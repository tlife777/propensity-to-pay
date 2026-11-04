#!/usr/bin/env python3
"""Join the decisions marked "For the presentation: yes", in order and with their charts, into docs/presentation.md."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECISIONS = ROOT / "docs" / "decisions"
OUTPUT = ROOT / "docs" / "presentation.md"

MARKED = re.compile(r"^For the presentation:\s*yes\s*$", re.IGNORECASE | re.MULTILINE)
MARKER_LINE = re.compile(r"^For the presentation:.*\n?", re.IGNORECASE | re.MULTILINE)
EVIDENCE_LINE = re.compile(r"^Evidence:(.*)$", re.MULTILINE)
FIGURE = re.compile(r"reports/figures/[^\s,;)]+\.(?:png|jpe?g|svg)", re.IGNORECASE)
FIELD = re.compile(r"^(Question|Options|Choice|Why|Evidence|Decided by):", re.MULTILINE)


def figures_in(text: str) -> list[str]:
    evidence = EVIDENCE_LINE.search(text)
    return FIGURE.findall(evidence.group(1)) if evidence else []


def section(text: str) -> str:
    body = MARKER_LINE.sub("", text).strip()
    body = FIELD.sub(r"\n**\1:**", body)
    body = re.sub(r"^# ", "## ", body, count=1)
    images = [f"![{Path(figure).stem}](../{figure})" for figure in figures_in(text)]
    return "\n\n".join([body, *images])


def main() -> None:
    paths = sorted(DECISIONS.glob("[0-9][0-9][0-9]-*.md"), key=lambda path: int(path.name[:3]))
    texts = [path.read_text(encoding="utf-8") for path in paths]
    marked = [text for text in texts if MARKED.search(text)]

    missing = [figure for text in marked for figure in figures_in(text) if not (ROOT / figure).exists()]
    if missing:
        sys.exit("Charts not found, presentation not written:\n" + "\n".join(missing))

    content = "\n\n".join(["# Decisions", *(section(text) for text in marked)]) + "\n"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(content, encoding="utf-8", newline="\n")
    print(f"{OUTPUT}: {len(marked)} of {len(texts)} decisions")


if __name__ == "__main__":
    main()
