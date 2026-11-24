"""Builds img/ for the site from the app icon and phone screenshots.

    python make_images.py

Screenshots are read from raw/ (1080x1920 PNGs named shot-map.png, shot-rule.png, shot-lucy.png,
shot-review.png, shot-ai.png, shot-light.png) and written as 540x960 JPEGs. Missing ones are skipped.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "img")
RAW = os.path.join(HERE, "raw")
ICON = r"C:\dev\bilingua-tutor\store\graphics\icon-512.png"
os.makedirs(IMG, exist_ok=True)

ic = Image.open(ICON).convert("RGBA")
for name, size in (("icon-192.png", 192), ("favicon.png", 48), ("apple-touch-icon.png", 180)):
    ic.resize((size, size), Image.LANCZOS).save(os.path.join(IMG, name))

shots = {}
for f in sorted(os.listdir(RAW)) if os.path.isdir(RAW) else []:
    if f.startswith("shot-") and f.endswith(".png"):
        im = Image.open(os.path.join(RAW, f)).convert("RGB")
        out = im.resize((540, 960), Image.LANCZOS)
        out.save(os.path.join(IMG, f[:-4] + ".jpg"), quality=84, optimize=True)
        shots[f[:-4]] = im
        print("shot", f)


def font(size, bold=False):
    for p in (r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
              r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


# Open Graph image 1200x630: dark Canal background, title left, two phones right
W, H = 1200, 630
bg = Image.new("RGB", (W, H), "#0a1419")
d = ImageDraw.Draw(bg)
for y in range(H):  # soft teal glow from the right
    pass
glow = Image.new("RGB", (W, H), "#0a1419")
gd = ImageDraw.Draw(glow)
gd.ellipse((560, -120, 1400, 760), fill="#0d3a3a")
from PIL import ImageFilter
glow = glow.filter(ImageFilter.GaussianBlur(120))
bg = Image.blend(bg, glow, 0.85)
d = ImageDraw.Draw(bg)
bg.paste(ic.resize((96, 96), Image.LANCZOS), (64, 70), ic.resize((96, 96), Image.LANCZOS))
d.text((178, 78), "Bilingua Tutor", font=font(54, True), fill="#e3edf0")
d.text((64, 230), "An AI language tutor", font=font(60, True), fill="#e3edf0")
d.text((64, 300), "that explains why.", font=font(60, True), fill="#2dd4bf")
d.text((64, 400), "Hand-written grammar map for Dutch, German,", font=font(28), fill="#a9bbc2")
d.text((64, 438), "Finnish, Hungarian and English. Runs on your", font=font(28), fill="#a9bbc2")
d.text((64, 476), "phone. No account, no ads.", font=font(28), fill="#a9bbc2")


def phone(im, x, y, w, rot=0):
    h = int(w * 16 / 9)
    s = im.resize((w, h), Image.LANCZOS)
    frame = Image.new("RGBA", (w + 16, h + 16), (0, 0, 0, 0))
    fd = ImageDraw.Draw(frame)
    fd.rounded_rectangle((0, 0, w + 15, h + 15), radius=34, fill="#05090c")
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, h - 1), radius=26, fill=255)
    frame.paste(s, (8, 8), mask)
    if rot:
        frame = frame.rotate(rot, expand=True, resample=Image.BICUBIC)
    bg.paste(frame, (x, y), frame)


if "shot-lucy" in shots and "shot-rule" in shots:
    phone(shots["shot-rule"], 690, 150, 250, 0)
    phone(shots["shot-lucy"], 930, 60, 250, 0)
bg.save(os.path.join(IMG, "og-image.jpg"), quality=88, optimize=True)
print("og-image written")
