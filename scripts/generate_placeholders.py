#!/usr/bin/env python3
"""
Generate labeled placeholder images for the Verve Intimate Society VIP portal.

These are intentionally lightweight, on-brand placeholders so the layout renders
cleanly before the real photography is dropped in. Re-run any time:

    python3 scripts/generate_placeholders.py

Swap real assets in by overwriting the files in assets/images and assets/logos
with the SAME filenames (see README.md → "Swapping in real assets").
"""
import os
from PIL import Image, ImageDraw, ImageFont

# ── Brand palette (from the design's CSS variables) ──────────────────────────
BLACK       = (20, 10, 8)       # --black   #140a08
PANEL       = (30, 17, 13)      # fallback panel tone used in the design
ACCENT      = (107, 30, 20)     # --accent  #6b1e14
ACCENT_PALE = (196, 168, 152)   # --accent-pale #c4a898
CREAM       = (245, 240, 234)   # --cream   #f5f0ea
BORDER      = (74, 44, 32)

IMG_DIR  = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
LOGO_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "logos")
os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(LOGO_DIR, exist_ok=True)


def _font(size, bold=False):
    """Load a serviceable TrueType font, falling back to PIL's default."""
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return ImageFont.load_default()


def _centered(draw, cx, y, text, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text((cx - w / 2, y), text, font=font, fill=fill)
    return bbox[3] - bbox[1]


def make_placeholder(filename, w, h, desc, *, bg=PANEL, fg=ACCENT_PALE,
                     watermark=True):
    img = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(img)
    cx = w / 2

    # Large faint "V" watermark, echoing the hero treatment
    if watermark:
        vf = _font(int(min(w, h) * 0.62), bold=True)
        vb = d.textbbox((0, 0), "V", font=vf)
        d.text((cx - (vb[2] - vb[0]) / 2, h / 2 - (vb[3] - vb[1]) / 2 - vb[1]),
               "V", font=vf, fill=(bg[0] + 14, bg[1] + 10, bg[2] + 8))

    # Inner hairline frame
    m = max(8, int(min(w, h) * 0.025))
    d.rectangle([m, m, w - m, h - m], outline=BORDER, width=2)

    # Text block, vertically centered
    f_tag   = _font(max(11, int(h * 0.030)))
    f_label = _font(max(16, int(h * 0.060)), bold=True)
    f_desc  = _font(max(12, int(h * 0.034)))
    f_dim   = _font(max(11, int(h * 0.030)))

    block_h = 0
    for fnt, txt, gap in [(f_tag, "PLACEHOLDER", 14),
                          (f_label, filename, 14),
                          (f_desc, desc, 12),
                          (f_dim, f"{w} × {h}px", 0)]:
        bb = d.textbbox((0, 0), txt, font=fnt)
        block_h += (bb[3] - bb[1]) + gap

    y = (h - block_h) / 2
    y += _centered(d, cx, y, "PLACEHOLDER", f_tag, ACCENT) + 14
    y += _centered(d, cx, y, filename, f_label, fg) + 14
    y += _centered(d, cx, y, desc, f_desc, (fg[0] - 30, fg[1] - 30, fg[2] - 30)) + 12
    _centered(d, cx, y, f"{w} × {h}px", f_dim, (150, 120, 108))

    path = os.path.join(IMG_DIR, filename)
    if filename.lower().endswith(".png"):
        img.save(path)
    else:
        img.save(path, quality=82)
    print(f"  {filename:18}  {w}x{h}")


# ── Image manifest: filename, w, h, short label, description ─────────────────
IMAGES = [
    ("img-hero.jpg",   1920, 1080, "hero",   "Studio interior · sofa + framed print (hero bg)"),
    ("img-studio.jpg", 1920,  860, "studio", "White bed studio set · full-width band"),
    ("img-banner.jpg", 1920, 1080, "banner", "Manifesto band · 'I am enough' mirror shot"),
    ("gallery-1.jpg",   700, 1000, "g1",     "Lingerie portrait · cropped body shot"),
    ("gallery-2.jpg",   700, 1000, "g2",     "Face portrait · woman on white sheets"),
    ("gallery-3.jpg",   700, 1000, "g3",     "Auburn half-face close crop"),
    ("gallery-4.jpg",   700, 1000, "g4",     "Portrait · fourth gallery panel"),
    ("ambassador.jpg",  960, 1180, "amb",    "B&W artistic seated portrait"),
    ("footer.jpg",     1920,  900, "footer", "Footer CTA background"),
    ("simpson.jpg",    1920,  900, "simpson","Return CTA banner background"),
    ("nannini.png",    1080,  360, "nannini","Feature panel (earn section)"),
]

print("Generating image placeholders → assets/images/")
for filename, w, h, _label, desc in IMAGES:
    make_placeholder(filename, w, h, desc=desc)

# Robe — lighter, product-style placeholder on cream
make_placeholder("robe-vi.png", 720, 900,
                 desc="Verve Intimate luxury robe (the referral gift)",
                 bg=CREAM, fg=ACCENT, watermark=False)

# ── Logo placeholders ────────────────────────────────────────────────────────
print("Generating logo placeholders → assets/logos/")


def make_logo(filename, w, h, bg, fg):
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0) if bg is None else bg)
    d = ImageDraw.Draw(img)
    cx, cy = w / 2, h / 2
    f1 = _font(int(h * 0.30), bold=True)
    f2 = _font(int(h * 0.14))
    b1 = d.textbbox((0, 0), "VERVE INTIMATE", font=f1)
    d.text((cx - (b1[2] - b1[0]) / 2, cy - (b1[3] - b1[1]) - 6),
           "VERVE INTIMATE", font=f1, fill=fg)
    b2 = d.textbbox((0, 0), "S O C I E T Y", font=f2)
    d.text((cx - (b2[2] - b2[0]) / 2, cy + 8), "S O C I E T Y", font=f2,
           fill=(fg[0], fg[1], fg[2], 200) if len(fg) == 4 else fg)
    img.save(os.path.join(LOGO_DIR, filename))
    print(f"  {filename}")


# Light wordmark for dark backgrounds (transparent bg), + dark wordmark for light
make_logo("logo-light.png", 900, 300, None, (245, 240, 234, 255))
make_logo("logo-dark.png",  900, 300, None, (20, 10, 8, 255))

# ── Favicon (brand "V") ──────────────────────────────────────────────────────
fav = Image.new("RGB", (256, 256), BLACK)
fd = ImageDraw.Draw(fav)
ff = _font(190, bold=True)
fb = fd.textbbox((0, 0), "V", font=ff)
fd.text((128 - (fb[2] - fb[0]) / 2 - fb[0], 128 - (fb[3] - fb[1]) / 2 - fb[1]),
        "V", font=ff, fill=ACCENT_PALE)
fav.save(os.path.join(IMG_DIR, "..", "favicon.png"))
print("Generating favicon → assets/favicon.png")
print("Done.")
