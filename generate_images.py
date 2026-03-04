from PIL import Image, ImageDraw, ImageFont
import json
import os

# Load JSON
with open("horoscopes.json", "r") as f:
    horoscopes = json.load(f)

# Make sure output folder exists
os.makedirs("images", exist_ok=True)

# Simple styling
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # default on Ubuntu runners
font = ImageFont.truetype(font_path, 28)

for entry in horoscopes:
    sign = entry["sign"]
    text = entry["horoscope"]

    # Create image
    img = Image.new("RGB", (800, 600), color=(255, 240, 230))
    draw = ImageDraw.Draw(img)
    draw.text((50, 50), f"{sign}\n{text}", fill=(0, 0, 0), font=font)

    # Save
    img_path = f"images/{sign.lower()}.png"
    img.save(img_path)
    print(f"Saved {img_path}")
