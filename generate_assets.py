import os
import urllib.request
from PIL import Image, ImageDraw, ImageFont

font_url = "https://github.com/google/fonts/raw/main/ofl/pressstart2p/PressStart2P-Regular.ttf"
font_path = "PressStart2P.ttf"

if not os.path.exists(font_path):
    try:
        urllib.request.urlretrieve(font_url, font_path)
    except Exception as e:
        print(f"Failed to download font: {e}")
        # fallback to a default font
        font_path = "arial.ttf"

def create_text_image(text_lines, filename, font_size=20, color="#FBD000", width=400, height=80, bg_color=None):
    img = Image.new('RGBA', (width, height), bg_color or (0,0,0,0))
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    
    # Calculate total height of text block
    total_height = len(text_lines) * font_size * 1.5
    y = (height - total_height) / 2
    
    for line in text_lines:
        bbox = d.textbbox((0,0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) / 2
        d.text((x, y), line, fill=color, font=font)
        y += font_size * 1.5

    img.save(os.path.join('assets', filename))
    print(f"Generated {filename}")

os.makedirs('assets', exist_ok=True)

# Intro
intro_lines = [
    "It's-a me, Wissa!",
    "Player 1 has entered!",
    "Press START to collaborate!"
]
create_text_image(intro_lines, "intro.png", font_size=14, color="#E8003D", width=600, height=80)

# Headings
create_text_image(["WHOAMI", "PLAYER INFO"], "head_whoami.png", font_size=20, color="#FBD000", width=400, height=70)
create_text_image(["TECH STACK", "POWER UPS"], "head_techstack.png", font_size=20, color="#FBD000", width=400, height=70)
create_text_image(["PORTFOLIO", "LEVELS UNLOCKED"], "head_portfolio.png", font_size=20, color="#FBD000", width=500, height=70)
create_text_image(["GITHUB STATS", "HIGH SCORES"], "head_github.png", font_size=20, color="#FBD000", width=500, height=70)
create_text_image(["CONTACT", "MULTIPLAYER"], "head_contact.png", font_size=20, color="#FBD000", width=400, height=70)

# Info Blocks
whoami_lines = [
    "NAME: Wissa Gamma E.L.",
    "ROLES: Fullstack, Mobile, NetEng",
    "STACK: NestJS, Next.js, Flutter",
    "BASED: Indonesia",
    "STATUS: Ready for Action!"
]
create_text_image(whoami_lines, "info_whoami.png", font_size=14, color="#FFFFFF", width=550, height=140)

portfolio_warn = ["WARNING: Most repos are PRIVATE", "Contains: Production APIs, internal tooling"]
create_text_image(portfolio_warn, "info_portfolio_warn.png", font_size=12, color="#E8003D", width=800, height=50)

portfolio_lines = [
    "[ REST API ] NestJS, Express",
    "[ MOBILE ] Flutter",
    "[ WEB ] Next.js, React",
    "[ INFRA ] Docker, AWS",
    "[ NETWORK ] Firewall, VPN"
]
create_text_image(portfolio_lines, "info_portfolio.png", font_size=14, color="#FFFFFF", width=800, height=150)

# Extras
create_text_image(["PLAYER 1"], "player1.png", font_size=12, color="#E8003D", width=130, height=30)
create_text_image(["> sudo make it work", "INSERT COIN"], "footer_sudo.png", font_size=16, color="#E8003D", width=400, height=60)
