"""Build the IMAGES map for wine/templates/cellar.html.

Published artifacts block images hotlinked from other sites, so bottle
photos have to be embedded in the page as data: URIs. This script downloads
each photo once, shrinks it to a small JPEG thumbnail, caches it under
--img-dir, and prints a JSON object {wine name: data URI} to paste over
`const IMAGES = {};` in cellar.html.

Input is a JSON file mapping each wine's exact name (as it appears in WINES
or HITLIST) to a source image URL:

    {"Example Estate Sauvignon Blanc": "https://example.com/bottle.jpg"}

Usage:
    python embed_images.py sources.json --img-dir wine/templates/img > images.json

Look at every downloaded thumbnail before using it: retailer pages often
serve an award badge or the wrong vintage as their product image.
Requires Pillow (pip install Pillow).
"""
import argparse
import base64
import io
import json
import os
import re
import sys
import urllib.request

from PIL import Image

THUMB_SIZE = (180, 260)  # about 2x the size the page displays


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def fetch_thumbnail(url, out_path):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req, timeout=30).read()
    im = Image.open(io.BytesIO(data))
    if im.mode in ("RGBA", "LA", "P"):
        # flatten transparency onto white so the bottle doesn't sit on black
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, "white")
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")
    im.thumbnail(THUMB_SIZE)
    im.save(out_path, "JPEG", quality=80, optimize=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("sources", help="JSON file: {wine name: image URL}")
    ap.add_argument("--img-dir", default="wine/templates/img",
                    help="where thumbnails are cached (default: %(default)s)")
    args = ap.parse_args()

    with open(args.sources, encoding="utf-8") as f:
        sources = json.load(f)
    os.makedirs(args.img_dir, exist_ok=True)

    images = {}
    for name, url in sources.items():
        path = os.path.join(args.img_dir, slug(name) + ".jpg")
        if not os.path.exists(path):
            try:
                fetch_thumbnail(url, path)
            except Exception as e:
                print("skipped %s: %s" % (name, e), file=sys.stderr)
                continue
        with open(path, "rb") as f:
            images[name] = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()

    json.dump(images, sys.stdout)
    print("\n%d of %d embedded" % (len(images), len(sources)), file=sys.stderr)


if __name__ == "__main__":
    main()
