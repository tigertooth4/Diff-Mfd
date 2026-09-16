"""Check original numbering, PDF links/assets and optionally render every page.

Run with uv run --with pymupdf --with pillow scripts/verify_reprint.py --render DIR.
The script reports progress and exits nonzero for structural failures.
"""
from pathlib import Path
import argparse
import collections
import json
import re
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--render", type=Path)
parser.add_argument("--jobname", choices=["main", "main_color"], default="main")
args = parser.parse_args()
errors = []
aux = (ROOT / "output" / f"{args.jobname}.aux").read_text()
labels = {}

def groups(text):
    result, depth, start = [], 0, 0
    for i, char in enumerate(text):
        if char == "{":
            if depth == 0:
                start = i + 1
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                result.append(text[start:i])
    return result

for line in aux.splitlines():
    if line.startswith(r"\newlabel{"):
        fields = groups(line[len(r"\newlabel"):])
        if len(fields) >= 2:
            if fields[0] in labels:
                errors.append(f"Duplicate label: {fields[0]}")
            labels[fields[0]] = groups(fields[1])

item_count = equation_count = 0
for chapter, last in enumerate([64, 34, 68, 19, 46, 36], 1):
    for number in range(1, last + 1):
        key = f"thm:{chapter}.{number}"
        expected = f"{chapter}.{number}"
        actual = labels.get(key, [None])[0]
        if actual != expected:
            errors.append(f"{key}: expected {expected}, got {actual}")
        item_count += 1
    text = (ROOT / f"chapters/chapter{chapter}.tex").read_text()
    if r"\subsection{\quad}" in text or r"\includegraphics" in text:
        errors.append(f"Chapter {chapter}: empty heading or old raster inclusion")
    for key, number in re.findall(r"\\label\{(eq:\d+\.\d+:(\d+))\}", text):
        actual = labels.get(key, [None])[0]
        if actual is None or actual.strip("{}") != number:
            errors.append(f"{key}: expected local tag {number}, got {actual}")
        equation_count += 1
    print(f"Source verification {chapter}/6", flush=True)

destinations = [v[3] for k, v in labels.items() if k.startswith("eq:") and len(v) > 3]
for key, count in collections.Counter(destinations).items():
    if count > 1:
        errors.append(f"Repeated equation destination: {key}")

log = (ROOT / "output" / f"{args.jobname}.log").read_text()
for pattern in [r"Overfull", r"Missing character", r"LaTeX Warning:.*undefined",
                r"multiply defined", r"LaTeX Font Warning", r"^!"]:
    if re.search(pattern, log, re.M):
        errors.append(f"Compile log matches {pattern}")
manifest = json.loads((ROOT / "figures/manifest.json").read_text())
for figure in manifest:
    source = ROOT / "figures" / figure["source"]
    if not source.is_file() or r"\includegraphics" in source.read_text():
        errors.append(f"Figure source missing or raster-based: {source}")
notation = json.loads((ROOT / "notation.json").read_text())
for entry in notation:
    if "thm:" + entry["item"] not in labels:
        errors.append(f"Missing notation target: {entry}")

doc = pymupdf.open(ROOT / "output" / f"{args.jobname}.pdf")
image_count = link_count = cover_image_count = 0
low_content = []
for i, page in enumerate(doc):
    image_count += len(page.get_images())
    if i == 0:
        cover_image_count = len(page.get_images())
    for link in page.get_links():
        link_count += 1
        if link["kind"] == pymupdf.LINK_GOTO and not 0 <= link["page"] < len(doc):
            errors.append(f"Broken PDF link on page {i+1}")
    if len(page.get_text().strip()) < 100:
        low_content.append(i + 1)
    if "\ufffd" in page.get_text():
        errors.append(f"Replacement glyph on page {i+1}")
allowed_cover_images = cover_image_count if args.jobname == "main_color" else 0
if image_count > allowed_cover_images:
    errors.append(f"PDF contains {image_count} raster image objects")

report = dict(pages=len(doc), original_items=item_count,
              local_equations=equation_count, redrawn_figures=len(manifest),
              notation_entries=len(notation), raster_images=image_count,
              cover_raster_images=cover_image_count,
              pdf_links=link_count, low_content_pages=low_content, errors=errors)
if args.render:
    from PIL import Image, ImageDraw
    args.render.mkdir(parents=True, exist_ok=True)
    for first in range(0, len(doc), 12):
        sheet = Image.new("RGB", (1440, 1590), "#d7d7d7")
        draw = ImageDraw.Draw(sheet)
        for j, index in enumerate(range(first, min(first + 12, len(doc)))):
            page = doc[index]
            pix = page.get_pixmap(matrix=pymupdf.Matrix(.57, .57), alpha=False)
            im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            x, y = j % 4 * 360, j // 4 * 530
            sheet.paste(im, (x + 10, y + 30))
            draw.text((x + 12, y + 8), f"PDF {index+1} / {page.get_label()}", fill="black")
        sheet.save(args.render / f"pages-{first+1:03}-{min(first+12,len(doc)):03}.jpg")
        print(f"Rendered {min(first+12,len(doc))}/{len(doc)} pages", flush=True)
    (args.render / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
raise SystemExit(bool(errors))
