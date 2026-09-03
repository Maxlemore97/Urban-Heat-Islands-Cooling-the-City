#!/usr/bin/env python3
"""Build the evidence bundle the report-audit subagents read.

Writes report.txt (the compiled PDF as text, with page markers) and metrics.json
(the formal numbers that need no judgement) into a scratch directory, and prints a
summary. Rebuilds the PDF first if it is older than any source file.

    python3 .claude/skills/report-audit/scripts/collect.py [--out DIR] [--no-build]
"""
import argparse, json, os, re, shutil, subprocess, sys
from pathlib import Path

TEMPLATE_HEADINGS = [
    "Introduction", "Challenge & Scoping", "Bio-Inspired Design Process",
    "Discovering & Abstracting", "Creating: Engineering Concept Development",
    "Concept Evaluation & Iteration", "Sustainability & Life's Principles",
    "Discussion & Conclusion", "References",
    "Appendix A -- AI Use Statement", "Appendix B -- Optional Supporting Material",
]


def find_root() -> Path:
    for c in (Path.cwd(), Path.cwd() / "Report_LaTeX", *Path.cwd().parents):
        if (c / "main.tex").is_file():
            return c
    sys.exit("main.tex not found — run this from the project root or Report_LaTeX/")


def stale(root: Path) -> bool:
    pdf = root / "main.pdf"
    if not pdf.is_file():
        return True
    newest = max((p.stat().st_mtime for p in [*root.glob("*.tex"),
                                              *root.glob("sections/*.tex"),
                                              *root.glob("*.bib")]), default=0)
    return newest > pdf.stat().st_mtime


def build(root: Path) -> None:
    if not shutil.which("latexmk"):
        print("  latexmk not found — using the existing main.pdf", file=sys.stderr)
        return
    subprocess.run(["latexmk", "-pdf", "-interaction=nonstopmode", "main.tex"],
                   cwd=root, capture_output=True)


def pdf_pages(root: Path, out: Path) -> int:
    """Write report.txt with one marker per page; return the page count."""
    if not shutil.which("pdftotext"):
        sys.exit("pdftotext not found (poppler). Install it or pass --no-build with a text dump.")
    n = 0
    log = (root / "main.log")
    if log.is_file():
        m = re.search(r"Output written on main\.pdf \((\d+) pages", log.read_text(errors="replace"))
        n = int(m.group(1)) if m else 0
    if not n:
        info = subprocess.run(["pdfinfo", str(root / "main.pdf")], capture_output=True, text=True)
        m = re.search(r"Pages:\s+(\d+)", info.stdout)
        n = int(m.group(1)) if m else 0
    chunks = []
    for p in range(1, n + 1):
        t = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), str(root / "main.pdf"), "-"],
                           capture_output=True, text=True).stdout
        chunks.append(f"=== PAGE {p} ===\n{t.rstrip()}\n")
    out.write_text("".join(chunks), encoding="utf-8")
    return n


def toc(root: Path):
    f = root / "main.toc"
    if not f.is_file():
        return []
    rows = []
    for line in f.read_text(errors="replace").splitlines():
        m = re.search(r"\{(section|subsection|subsubsection)\}\{(?:\\numberline \{([\d.]+)\})?(.*?)\}\{(\d+)\}", line)
        if m:
            level, num, title, page = m.groups()
            title = re.sub(r"\\([&%$#_])", r"\1", title)          # \& -> &
            title = re.sub(r"\\[a-zA-Z]+\s*|[{}]", "", title)
            title = re.sub(r"\s+", " ", title).replace("\u2019", "'").strip()
            rows.append({"level": level, "number": num or "", "title": title, "page": int(page)})
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.environ.get("CLAUDE_SCRATCHPAD", "") or "report-audit")
    ap.add_argument("--no-build", action="store_true")
    a = ap.parse_args()

    root = find_root()
    out = Path(a.out) / "report-audit" if a.out.endswith("scratchpad") else Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    if not a.no_build and stale(root):
        print("PDF is older than the sources — rebuilding")
        build(root)

    pages = pdf_pages(root, out / "report.txt")
    entries = toc(root)

    # body = first page of section 1 .. last page before References
    starts = {e["number"]: e["page"] for e in entries if e["level"] == "section" and e["number"]}
    refs = next((e["page"] for e in entries if e["title"].startswith("References")), pages)
    body_first = starts.get("1", 1)
    body_pages = max(0, refs - body_first)

    tex = {p.name: p.read_text(errors="replace") for p in sorted((root / "sections").glob("*.tex"))}
    todos = {n: len(re.findall(r"\\todo\{", t)) for n, t in tex.items()}

    bib = (root / "references.bib").read_text(errors="replace") if (root / "references.bib").is_file() else ""
    bib_keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib))
    cited = set()
    for t in tex.values():
        for grp in re.findall(r"\\(?:paren|text|foot|auto)cite\s*(?:\[[^\]]*\])*\{([^}]*)\}", t):
            cited |= {k.strip() for k in grp.split(",") if k.strip()}

    titles = [e["title"] for e in entries]
    missing_headings = [h for h in TEMPLATE_HEADINGS
                        if not any(h.lower().replace("--", "-") in t.lower().replace("--", "-")
                                   or t.lower() in h.lower() for t in titles)]

    metrics = {
        "root": str(root),
        "pdf_pages_total": pages,
        "body_pages": body_pages,
        "body_page_guideline": "15-25 excluding references and appendices",
        "body_within_guideline": 15 <= body_pages <= 25,
        "sections": entries,
        "todo_total": sum(todos.values()),
        "todo_by_file": todos,
        "figures": sum(len(re.findall(r"\\begin\{figure\}", t)) for t in tex.values()),
        "tables": sum(len(re.findall(r"\\begin\{(?:table|longtable)\}", t)) for t in tex.values()),
        "equations": sum(len(re.findall(r"\\begin\{(?:equation|align)\}", t)) for t in tex.values()),
        "bib_entries": len(bib_keys),
        "bib_cited": len(cited & bib_keys),
        "bib_uncited": sorted(bib_keys - cited),
        "cited_but_missing": sorted(cited - bib_keys),
        "template_headings_not_found": missing_headings,
    }
    (out / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    print(f"bundle      {out}")
    print(f"pages       {pages} total, {body_pages} body "
          f"({'within' if metrics['body_within_guideline'] else 'OUTSIDE'} the 15-25 guideline)")
    print(f"figures     {metrics['figures']}   tables {metrics['tables']}   equations {metrics['equations']}")
    print(f"todos       {metrics['todo_total']}  " +
          "  ".join(f"{n.split('_')[0]}:{c}" for n, c in todos.items() if c))
    print(f"references  {metrics['bib_cited']}/{metrics['bib_entries']} cited"
          + (f", uncited: {', '.join(metrics['bib_uncited'])}" if metrics["bib_uncited"] else ""))
    if metrics["cited_but_missing"]:
        print(f"BROKEN      cited but not in the .bib: {', '.join(metrics['cited_but_missing'])}")
    if missing_headings:
        print(f"HEADINGS    template headings not found: {'; '.join(missing_headings)}")


if __name__ == "__main__":
    main()
