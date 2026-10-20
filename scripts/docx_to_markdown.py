#!/usr/bin/env python3
"""Convert archive/canvas-submissions/*.docx to docs/*.md (readable on GitHub)."""

from __future__ import annotations

import re
from pathlib import Path

from docx import Document

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive" / "canvas-submissions"
DOCS = ROOT / "docs"

SLUGS: dict[str, str] = {
    "git setup.docx": "git-setup.md",
    "git data model.docx": "git-data-model.md",
    "Git Cheat Sheet.docx": "git-cheat-sheet.md",
    "Git Cheat Sheet-1.docx": "git-cheat-sheet-supplement.md",
    "linux shell.docx": "linux-shell.md",
    "Class Exercise.docx": "class-exercise.md",
    "class exercise feb7.docx": "class-exercise-feb7.md",
    "problem.docx": "problem-statement.md",
    "What People Say.docx": "what-people-say.md",
    "Document1.docx": "document-notes.md",
    "Doc1.docx": "doc1-notes.md",
    "Doc1-1.docx": "doc1-notes-part1.md",
    "Doc1-2.docx": "doc1-notes-part2.md",
}


def para_to_md(text: str) -> str:
    text = text.strip()
    if not text:
        return ""
    if text.startswith("#"):
        return text
    return text


def convert_docx(src: Path, dest: Path, title: str) -> None:
    doc = Document(src)
    lines: list[str] = [
        f"# {title}",
        "",
        f"**Source:** [`{src.name}`](../archive/canvas-submissions/{src.name.replace(' ', '%20')})  ",
        "**Course:** COSC 381 - Software Engineering Solutions (EMU)  ",
        "**Author:** Julio Barros",
        "",
    ]
    for para in doc.paragraphs:
        t = para_to_md(para.text)
        if not t:
            lines.append("")
            continue
        style = (para.style.name or "").lower()
        if "heading 1" in style:
            lines.extend(["", f"## {t}", ""])
        elif "heading 2" in style:
            lines.extend(["", f"### {t}", ""])
        elif "heading 3" in style:
            lines.extend(["", f"#### {t}", ""])
        elif "list" in style:
            lines.append(f"- {t}")
        else:
            lines.append(t)
            lines.append("")

    body = "\n".join(lines)
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(body, encoding="utf-8")


def main() -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    for name, slug in SLUGS.items():
        src = ARCHIVE / name
        if not src.exists():
            print(f"skip missing {name}")
            continue
        title = name.removesuffix(".docx")
        convert_docx(src, DOCS / slug, title)
        print(f"wrote docs/{slug}")


if __name__ == "__main__":
    main()
