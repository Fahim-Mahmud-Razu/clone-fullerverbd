from PIL import Image, ImageDraw, ImageFont

SRC_IMG_PATH = '/home/razu/.gemini/antigravity-ide/brain/cfec9644-f401-4f74-8a53-9f0e4099dd93/.user_uploaded/media_1792238902681.png'
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

shield_crop = make_transparent(src.crop((274, 65, 761, 630)))
text_crop = make_transparent(src.crop((165, 635, 888, 908)))
stacked_crop = make_transparent(src.crop((165, 65, 888, 908)))

# Save standard dark text logos
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
stacked_crop.save('public/front-end/img/max-logo-stacked.png')

# Create white-text versions for dark backgrounds
def make_white_text_version(im):
    im_w = im.copy()
    data = im_w.load()
    w, h = im_w.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = data[x, y]
            if a > 0:
                # If pixel is navy (low red, low green, medium blue)
                if r < 70 and g < 90 and b > 40:
                    # turn into pure white preserving alpha
                    data[x, y] = (255, 255, 255, a)
                # Orange pixels stay bright orange
    return im_w

horiz_white = make_white_text_version(horiz)
horiz_white.save('public/front-end/img/max-logo-horizontal-white.png')

stacked_white = make_white_text_version(stacked_crop)
stacked_white.save('public/front-end/img/max-logo-stacked-white.png')
print("Saved white versions of logos!")

# Now regenerate max_banner1.png cleanly
orig_banner = Image.open('public/front-end/img/slider/Fullever_Banner1.png').convert('RGBA')
banner = orig_banner.copy()
draw_b = ImageDraw.Draw(banner)

# 1. Fill left navy curve
for y in range(700):
    rx = 860 + int(60 * (1 - (abs(y - 350) / 350.0)**2))
    draw_b.line([(0, y), (rx, y)], fill=(5, 37, 79, 255))
    # orange border
    draw_b.line([(rx, y), (rx + 14, y)], fill=(246, 98, 2, 255))

# 2. Cover the bottom bar entirely (y: 600..700, x: 0..1350)
draw_b.rectangle([(0, 610), (1350, 700)], fill=(3, 24, 52, 255))
draw_b.line([(0, 610), (1350, 610)], fill=(246, 98, 2, 255), width=3)

# 3. Paste white horizontal logo
b_logo = horiz_white.resize((int(horiz_white.width * 0.75), int(horiz_white.height * 0.75)), Image.Resampling.LANCZOS)
banner.paste(b_logo, (60, 50), b_logo)

try:
    bf_welcome = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 34)
    bf_company = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 44)
    bf_desc = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    bf_contact_bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    bf_contact_norm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
except Exception:
    bf_welcome = bf_company = bf_desc = bf_contact_bold = bf_contact_norm = None

draw_b.text((60, 260), "Welcome to", fill=(246, 98, 2), font=bf_welcome)
draw_b.text((60, 310), "MAX GLOVES BD LTD.", fill=(255, 255, 255), font=bf_company)

draw_b.text((60, 385), "We are committed to delivering high-quality leather gloves", fill=(215, 228, 245), font=bf_desc)
draw_b.text((60, 415), "that ensure safety, comfort, and reliability for every task.", fill=(215, 228, 245), font=bf_desc)
draw_b.text((60, 445), "Protecting Hands, Building Futures.", fill=(246, 98, 2), font=bf_desc)

# Middle feature badges
draw_b.rectangle([(60, 500), (280, 550)], fill=(8, 48, 98), outline=(246, 98, 2), width=1)
draw_b.text((170, 525), "PREMIUM LEATHER", fill=(255, 255, 255), font=bf_contact_bold, anchor="mm")

draw_b.rectangle([(300, 500), (520, 550)], fill=(8, 48, 98), outline=(246, 98, 2), width=1)
draw_b.text((410, 525), "GLOBAL EXPORTS", fill=(255, 255, 255), font=bf_contact_bold, anchor="mm")

draw_b.rectangle([(540, 500), (760, 550)], fill=(8, 48, 98), outline=(246, 98, 2), width=1)
draw_b.text((650, 525), "OEM / ODM READY", fill=(255, 255, 255), font=bf_contact_bold, anchor="mm")

# Bottom Bar Info (crisp white and orange text)
# Location
draw_b.text((60, 640), "Factory:", fill=(246, 98, 2), font=bf_contact_bold)
draw_b.text((140, 640), "Savar, Hemayetpur", fill=(255, 255, 255), font=bf_contact_norm)

# Email
draw_b.text((370, 640), "Email:", fill=(246, 98, 2), font=bf_contact_bold)
draw_b.text((435, 640), "maxglovesbdltd@gmail.com", fill=(255, 255, 255), font=bf_contact_norm)

# Website
draw_b.text((740, 640), "Web:", fill=(246, 98, 2), font=bf_contact_bold)
draw_b.text((795, 640), "www.maxglovesbdltd.com", fill=(255, 255, 255), font=bf_contact_norm)

# Phone
draw_b.text((1060, 640), "Phone:", fill=(246, 98, 2), font=bf_contact_bold)
draw_b.text((1130, 640), "+880 1710-591088", fill=(255, 255, 255), font=bf_contact_norm)

banner.save('public/front-end/img/slider/max_banner1.png')
print("Banner 1 updated with complete clean coverage and real phone!")

# Regenerate visiting card with real info
card = Image.new('RGBA', (1000, 600), (255, 255, 255, 255))
draw_card = ImageDraw.Draw(card)
draw_card.polygon([(700, 600), (1000, 480), (1000, 600)], fill=(5, 37, 79, 255))
draw_card.polygon([(760, 600), (1000, 520), (1000, 600)], fill=(246, 98, 2, 255))
draw_card.polygon([(920, 0), (1000, 0), (1000, 80)], fill=(5, 37, 79, 120))

scale_c = 110 / horiz.height
cw = int(horiz.width * scale_c)
ch = 110
logo_res = horiz.resize((cw, ch), Image.Resampling.LANCZOS)
card.paste(logo_res, (60, 45), logo_res)

draw_card.rectangle([(60, 185), (66, 305)], fill=(246, 98, 2, 255))
font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 34)
font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
font_role = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
font_info = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 19)
font_info_b = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 19)

draw_card.text((85, 190), "[CONTACT PERSON]", fill=(5, 37, 79), font=font_large)
draw_card.text((85, 235), "Sales & Marketing", fill=(246, 98, 2), font=font_sub)
draw_card.text((85, 270), "Max Gloves BD Ltd.", fill=(80, 80, 80), font=font_role)

card_items = [
    ("Phone:", "+880 1710-591088"),
    ("Email:", "maxglovesbdltd@gmail.com"),
    ("Website:", "www.maxglovesbdltd.com"),
    ("Office:", "585/C, Khilgaon, C Block, Dhaka-1219"),
    ("Factory:", "Savar, Hemayetpur, Dhaka, Bangladesh")
]

y_pos = 330
for label, val in card_items:
    draw_card.text((60, y_pos), label, fill=(246, 98, 2), font=font_info_b)
    draw_card.text((155, y_pos), val, fill=(30, 30, 30), font=font_info)
    y_pos += 42

card.save('public/front-end/img/max-visiting-card.png')
print("Saved updated max-visiting-card.png")

# Regenerate cover graphic with real info
cover = Image.new('RGB', (1000, 1500), (5, 37, 79))
draw_cover = ImageDraw.Draw(cover)
draw_cover.rectangle([(30, 30), (970, 1470)], outline=(246, 98, 2), width=3)
draw_cover.rectangle([(45, 45), (955, 1455)], outline=(20, 60, 110), width=2)

scale_cov = 550 / stacked_crop.height
cov_w = int(stacked_crop.width * scale_cov)
cov_h = 550
stacked_cov = stacked_crop.resize((cov_w, cov_h), Image.Resampling.LANCZOS)
cov_x = (1000 - cov_w) // 2
cover.paste(stacked_cov, (cov_x, 180), stacked_cov)

draw_cover.rectangle([(30, 1100), (970, 1470)], fill=(3, 27, 58))
draw_cover.line([(30, 1100), (970, 1100)], fill=(246, 98, 2), width=4)

cov_f1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 34)
cov_f2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 21)
cov_tag = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 25)

draw_cover.text((500, 1145), "MAX GLOVES BD LTD.", fill=(255, 255, 255), font=cov_f1, anchor="mm")
draw_cover.text((500, 1195), "PROTECTING HANDS, BUILDING FUTURES", fill=(246, 98, 2), font=cov_tag, anchor="mm")
draw_cover.text((500, 1250), "Phone: +880 1710-591088  |  maxglovesbdltd@gmail.com", fill=(220, 220, 220), font=cov_f2, anchor="mm")
draw_cover.text((500, 1300), "Office: 585/C, Khilgaon, C Block, Dhaka-1219", fill=(220, 220, 220), font=cov_f2, anchor="mm")
draw_cover.text((500, 1350), "Factory: Savar, Hemayetpur, Dhaka, Bangladesh", fill=(220, 220, 220), font=cov_f2, anchor="mm")
draw_cover.text((500, 1400), "www.maxglovesbdltd.com", fill=(246, 98, 2), font=cov_f2, anchor="mm")

cover.save('public/front-end/img/max_cover.png')
print("Saved updated max_cover.png")

