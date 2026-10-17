import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

SRC_IMG_PATH = '/home/razu/.gemini/antigravity-ide/brain/cfec9644-f401-4f74-8a53-9f0e4099dd93/.user_uploaded/media_1792238902681.png'
NAVY = (5, 37, 79, 255)       # #05254F
ORANGE = (246, 98, 2, 255)    # #F66202
WHITE = (255, 255, 255, 255)

src = Image.open(SRC_IMG_PATH).convert('RGBA')

def make_transparent(im):
    im = im.copy()
    data = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = data[x, y]
            diff = max(255 - r, 255 - g, 255 - b)
            if diff < 12:
                data[x, y] = (r, g, b, 0)
            elif diff < 42:
                alpha = int(255 * (diff - 12) / 30.0)
                data[x, y] = (r, g, b, alpha)
    return im

print("1. Extracting base transparent crops...")
# Shield box: (279, 70, 756, 625) -> padding (274, 65, 761, 630)
shield_crop = make_transparent(src.crop((274, 65, 761, 630)))

# Text box: MAX, GLOVES BD LTD, Tagline: (165, 635, 888, 908)
text_crop = make_transparent(src.crop((165, 635, 888, 908)))

# Stacked logo: (165, 65, 888, 908)
stacked_crop = make_transparent(src.crop((165, 65, 888, 908)))

os.makedirs('public/front-end/img/slider', exist_ok=True)
os.makedirs('public/front-end/img/gallery', exist_ok=True)

# Save stacked logo
stacked_crop.save('public/front-end/img/max-logo-stacked.png')
print("Saved max-logo-stacked.png")

# Save shield only
shield_crop.save('public/front-end/img/max-shield.png')
print("Saved max-shield.png")

# 2. Horizontal lockup
# Shield left, text right
target_h = 240
shield_scale = target_h / shield_crop.height
sw = int(shield_crop.width * shield_scale)
sh = target_h
shield_resized = shield_crop.resize((sw, sh), Image.Resampling.LANCZOS)

text_scale = (target_h * 0.95) / text_crop.height
tw = int(text_crop.width * text_scale)
th = int(text_crop.height * text_scale)
text_resized = text_crop.resize((tw, th), Image.Resampling.LANCZOS)

gap = 40
horiz_w = sw + gap + tw
horiz_h = target_h
horiz = Image.new('RGBA', (horiz_w, horiz_h), (0, 0, 0, 0))
horiz.paste(shield_resized, (0, 0), shield_resized)
y_offset = (horiz_h - th) // 2
horiz.paste(text_resized, (sw + gap, y_offset), text_resized)
horiz.save('public/front-end/img/max-logo-horizontal.png')
print("Saved max-logo-horizontal.png")

# 3. Watermark (shield at 6% opacity)
watermark = shield_crop.copy()
wm_data = watermark.load()
for y in range(watermark.height):
    for x in range(watermark.width):
        r, g, b, a = wm_data[x, y]
        if a > 0:
            wm_data[x, y] = (r, g, b, int(a * 0.06))
watermark.save('public/front-end/img/max-watermark.png')
print("Saved max-watermark.png")

# 4. Favicon and App Icons
# For square icons, put shield centered on transparent background with a slight margin
def create_square_icon(size):
    icon = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    margin = int(size * 0.08)
    inner_size = size - 2 * margin
    scale = inner_size / max(shield_crop.width, shield_crop.height)
    iw = int(shield_crop.width * scale)
    ih = int(shield_crop.height * scale)
    sh_res = shield_crop.resize((iw, ih), Image.Resampling.LANCZOS)
    x = (size - iw) // 2
    y = (size - ih) // 2
    icon.paste(sh_res, (x, y), sh_res)
    return icon

create_square_icon(16).save('public/favicon-16x16.png')
create_square_icon(32).save('public/favicon-32x32.png')
create_square_icon(48).save('public/favicon-48x48.png')
create_square_icon(180).save('public/apple-touch-icon.png')
create_square_icon(192).save('public/icon-192x192.png')
create_square_icon(512).save('public/icon-512x512.png')
create_square_icon(32).save('public/favicon.ico', format='ICO')
create_square_icon(32).save('public/front-end/img/favicon.png')
print("Saved all favicons and icons!")

# 5. Visiting Card for modal
# 1000 x 600 card
card = Image.new('RGBA', (1000, 600), (255, 255, 255, 255))
draw = ImageDraw.Draw(card)

# Draw subtle background pattern / corner wave in navy & orange
# Bottom-right swoosh
draw.polygon([(700, 600), (1000, 480), (1000, 600)], fill=(5, 37, 79, 255))
draw.polygon([(760, 600), (1000, 520), (1000, 600)], fill=(246, 98, 2, 255))

# Top-right subtle accent
draw.polygon([(920, 0), (1000, 0), (1000, 80)], fill=(5, 37, 79, 120))

# Place horizontal logo on top left
scale_c = 110 / horiz.height
cw = int(horiz.width * scale_c)
ch = 110
logo_res = horiz.resize((cw, ch), Image.Resampling.LANCZOS)
card.paste(logo_res, (60, 50), logo_res)

# Left vertical accent line
draw.rectangle([(60, 200), (66, 320)], fill=(246, 98, 2, 255))

# Use system font
try:
    font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
    font_role = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    font_info = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    font_info_b = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
except Exception:
    font_large = font_sub = font_role = font_info = font_info_b = None

draw.text((85, 205), "[CONTACT PERSON]", fill=(5, 37, 79), font=font_large)
draw.text((85, 255), "Sales & Marketing", fill=(246, 98, 2), font=font_sub)
draw.text((85, 290), "Max Gloves BD Ltd.", fill=(80, 80, 80), font=font_role)

# Contact info block with labels
items = [
    ("Factory:", "Savar, Hemayetpur"),
    ("Email:", "maxglovesbdltd@gmail.com"),
    ("Website:", "www.maxglovesbdltd.com"),
    ("Phone:", "[PHONE]"),
    ("Office:", "[OFFICE ADDRESS]")
]

y_pos = 360
for label, val in items:
    draw.text((60, y_pos), label, fill=(246, 98, 2), font=font_info_b)
    draw.text((170, y_pos), val, fill=(30, 30, 30), font=font_info)
    y_pos += 42

card.save('public/front-end/img/max-visiting-card.png')
print("Saved max-visiting-card.png")

# 6. About Page Cover Graphic (replacing public/front-end/img/gallery/Cover.png)
cover = Image.new('RGB', (1000, 1500), (5, 37, 79))
draw_cover = ImageDraw.Draw(cover)

# Draw elegant borders and orange geometric accent lines
draw_cover.rectangle([(30, 30), (970, 1470)], outline=(246, 98, 2), width=3)
draw_cover.rectangle([(45, 45), (955, 1455)], outline=(20, 60, 110), width=2)

# Place large stacked logo in the center
scale_cov = 550 / stacked_crop.height
cov_w = int(stacked_crop.width * scale_cov)
cov_h = 550
stacked_cov = stacked_crop.resize((cov_w, cov_h), Image.Resampling.LANCZOS)
cov_x = (1000 - cov_w) // 2
cover.paste(stacked_cov, (cov_x, 200), stacked_cov)

# Bottom banner bar
draw_cover.rectangle([(30, 1150), (970, 1470)], fill=(3, 27, 58))
draw_cover.line([(30, 1150), (970, 1150)], fill=(246, 98, 2), width=4)

try:
    cov_f1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 34)
    cov_f2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
    cov_tag = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
except Exception:
    cov_f1 = cov_f2 = cov_tag = None

draw_cover.text((500, 1200), "MAX GLOVES BD LTD.", fill=(255, 255, 255), font=cov_f1, anchor="mm")
draw_cover.text((500, 1255), "PROTECTING HANDS, BUILDING FUTURES", fill=(246, 98, 2), font=cov_tag, anchor="mm")
draw_cover.text((500, 1315), "Factory: Savar, Hemayetpur", fill=(220, 220, 220), font=cov_f2, anchor="mm")
draw_cover.text((500, 1365), "maxglovesbdltd@gmail.com  |  www.maxglovesbdltd.com", fill=(220, 220, 220), font=cov_f2, anchor="mm")
draw_cover.text((500, 1415), "Phone: [PHONE]", fill=(246, 98, 2), font=cov_f2, anchor="mm")

cover.save('public/front-end/img/max_cover.png')
print("Saved max_cover.png")

# 7. Hero Slider Banner 1 (1920x700)
# Rebranding slider/Fullever_Banner1.png
orig_banner = Image.open('public/front-end/img/slider/Fullever_Banner1.png').convert('RGBA')
# The original banner has glove photos and factory building on right (x > 800)
# Left side (x: 0..850) is dark navy with old text and old logo.
# We will composite a crisp dark navy curved panel on the left with Max Gloves branding!
banner = orig_banner.copy()
draw_b = ImageDraw.Draw(banner)

# Fill left navy section smoothly
for y in range(700):
    # curve from x=0 to x=860
    # parabolic curve
    rx = 840 + int(60 * (1 - (abs(y - 350) / 350.0)**2))
    draw_b.line([(0, y), (rx, y)], fill=(5, 37, 79, 255))

# Draw the red/orange swoosh separator
for y in range(700):
    rx = 840 + int(60 * (1 - (abs(y - 350) / 350.0)**2))
    draw_b.line([(rx, y), (rx + 14, y)], fill=(246, 98, 2, 255))

# Paste horizontal logo on the left
b_logo = horiz.resize((int(horiz.width * 0.7), int(horiz.height * 0.7)), Image.Resampling.LANCZOS)
banner.paste(b_logo, (60, 60), b_logo)

try:
    bf_welcome = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    bf_company = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 46)
    bf_desc = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    bf_contact = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
except Exception:
    bf_welcome = bf_company = bf_desc = bf_contact = None

draw_b.text((60, 270), "Welcome to", fill=(246, 98, 2), font=bf_welcome)
draw_b.text((60, 320), "MAX GLOVES BD LTD.", fill=(255, 255, 255), font=bf_company)

draw_b.text((60, 395), "We are committed to delivering high-quality leather gloves", fill=(210, 225, 245), font=bf_desc)
draw_b.text((60, 425), "that ensure safety, comfort, and reliability for every task.", fill=(210, 225, 245), font=bf_desc)
draw_b.text((60, 455), "Protecting Hands, Building Futures.", fill=(246, 98, 2), font=bf_desc)

# Bottom contact pill
draw_b.rectangle([(50, 560), (780, 640)], fill=(3, 24, 52, 240), outline=(246, 98, 2, 255), width=2)
draw_b.text((70, 580), "Factory: Savar, Hemayetpur", fill=(255, 255, 255), font=bf_contact)
draw_b.text((70, 610), "maxglovesbdltd@gmail.com", fill=(246, 98, 2), font=bf_contact)
draw_b.text((440, 580), "www.maxglovesbdltd.com", fill=(255, 255, 255), font=bf_contact)
draw_b.text((440, 610), "Phone: [PHONE]", fill=(246, 98, 2), font=bf_contact)

banner.save('public/front-end/img/slider/max_banner1.png')
print("Saved max_banner1.png")

# 8. Split Gloves slide rebranding (public/front-end/img/slider/max_split_gloves.jpg)
orig_split = Image.open('public/front-end/img/slider/FULLEVER_SPLIT_GLOVES_1920x700_150kb.jpg').convert('RGBA')
draw_s = ImageDraw.Draw(orig_split)

# In orig_split:
# Bottom right (x: 1450..1920, y: 620..700) has "www.fulleverbd.com" on orange background
draw_s.rectangle([(1450, 630), (1920, 700)], fill=(246, 98, 2, 255))
try:
    web_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
except Exception:
    web_font = None

draw_s.text((1500, 650), "www.maxglovesbdltd.com", fill=(255, 255, 255), font=web_font)

# Replace top right badge icon if present
badge_scale = 55 / shield_crop.height
bw = int(shield_crop.width * badge_scale)
bh = 55
sh_badge = shield_crop.resize((bw, bh), Image.Resampling.LANCZOS)
orig_split.paste(sh_badge, (1535, 45), sh_badge)

orig_split.convert('RGB').save('public/front-end/img/slider/max_split_gloves.jpg', quality=95)
print("Saved max_split_gloves.jpg")

print("ALL BRAND ASSETS GENERATED SUCCESSFULLY!")
