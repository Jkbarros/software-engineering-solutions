#!/usr/bin/env python3
"""Generate docs/demo.gif — Git workflow sketch for the README."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "demo.gif"
W, H = 720, 200
DURATION_MS = 2000

BG = (15, 23, 42)
PANEL = (30, 41, 59)
ACCENT = (56, 189, 248)
OK = (74, 222, 128)
TEXT = (226, 232, 240)


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for name in ("consola.ttf", "Consolas.ttf", "cour.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def frame(title: str, body: str, status: str | None = None, status_color: int = OK) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    title_font = load_font(22)
    body_font = load_font(16)
    draw.rounded_rectangle((24, 24, W - 24, H - 24), radius=12, fill=PANEL)
    draw.text((40, 36), title, fill=ACCENT, font=title_font)
    draw.text((40, 78), body, fill=TEXT, font=body_font)
    if status:
        draw.text((40, 130), status, fill=status_color, font=body_font)
    return img


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    frames = [
        frame("1. Working tree", "edit files  →  git status", None),
        frame("2. Stage & commit", "git add -p  →  git commit", "message: describe the change", ACCENT),
        frame("3. Share", "git push origin main", "remote: GitHub / team repo", OK),
    ]
    frames[0].save(
        OUT,
        save_all=True,
        append_images=frames[1:],
        duration=DURATION_MS,
        loop=0,
        optimize=True,
    )
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
