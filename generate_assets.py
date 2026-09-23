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

def create_mario_banner(text_lines, filename, font_size=16, text_color="#FFFFFF", bg_color="#000000", border_color="#FFFFFF", width=600, height=None, border_width=6, padding=30):
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    
    # Calculate height if not provided
    if height is None:
        height = padding * 2 + (len(text_lines) * font_size * 1.5)
    
    # Create image
    img = Image.new('RGBA', (width, int(height)), (0,0,0,0))
    d = ImageDraw.Draw(img)
    
    # Draw Mario-style UI Box
    
    # 1. Outer shadow/dark border (optional, let's keep it simple with 1 outer border)
    d.rectangle([(0, 0), (width-1, int(height)-1)], fill="#000000") # Base black outline
    
    # 2. Main border (White)
    d.rectangle([(2, 2), (width-3, int(height)-3)], fill=border_color)
    
    # 3. Inner shadow/dark border (creates depth)
    d.rectangle([(border_width+2, border_width+2), (width-3-border_width, int(height)-3-border_width)], fill="#000000")
    
    # 4. Background color
    d.rectangle([(border_width+4, border_width+4), (width-5-border_width, int(height)-5-border_width)], fill=bg_color)
    
    # 5. Corner "screws" (classic 8-bit UI detail)
    cs = 4 # corner size
    b = border_width + 4 # background start
    d.rectangle([(b+cs, b+cs), (b+cs+3, b+cs+3)], fill=border_color) # Top-left
    d.rectangle([(width-b-cs-4, b+cs), (width-b-cs-1, b+cs+3)], fill=border_color) # Top-right
    d.rectangle([(b+cs, int(height)-b-cs-4), (b+cs+3, int(height)-b-cs-1)], fill=border_color) # Bottom-left
    d.rectangle([(width-b-cs-4, int(height)-b-cs-4), (width-b-cs-1, int(height)-b-cs-1)], fill=border_color) # Bottom-right

    # Draw text
    total_text_height = len(text_lines) * font_size * 1.5
    y = (int(height) - total_text_height) / 2
    
    for line in text_lines:
        bbox = d.textbbox((0,0), line, font=font)
        text_w = bbox[2] - bbox[0]
        x = (width - text_w) / 2
        d.text((x, y), line, fill=text_color, font=font)
        y += font_size * 1.5
        
    os.makedirs('assets', exist_ok=True)
    img.save(os.path.join('assets', filename))
    print(f"Generated {filename}")

# Headings (Red bg, white border, yellow text)
create_mario_banner(["WHOAMI", "PLAYER INFO"], "head_whoami.png", font_size=20, text_color="#FBD000", bg_color="#E8003D", width=500, height=90)
create_mario_banner(["TECH STACK", "POWER UPS"], "head_techstack.png", font_size=20, text_color="#FBD000", bg_color="#E8003D", width=500, height=90)
create_mario_banner(["PORTFOLIO", "LEVELS UNLOCKED"], "head_portfolio.png", font_size=20, text_color="#FBD000", bg_color="#E8003D", width=600, height=90)
create_mario_banner(["GITHUB STATS", "HIGH SCORES"], "head_github.png", font_size=20, text_color="#FBD000", bg_color="#E8003D", width=550, height=90)
create_mario_banner(["CONTACT", "MULTIPLAYER"], "head_contact.png", font_size=20, text_color="#FBD000", bg_color="#E8003D", width=500, height=90)

# Info blocks (Black bg, white text)
whoami_lines = [
    "NAME: Wissa Gamma E.L.",
    "ROLES: Fullstack, Mobile, NetEng",
    "STACK: NestJS, Next.js, Flutter",
    "BASED: Indonesia",
    "STATUS: Ready for Action!"
]
create_mario_banner(whoami_lines, "info_whoami.png", font_size=16, text_color="#FFFFFF", bg_color="#000000", width=700)

portfolio_lines = [
    "[ REST API ] NestJS, Express",
    "[ MOBILE ] Flutter",
    "[ WEB ] Next.js, React",
    "[ INFRA ] Docker, AWS",
    "[ NETWORK ] Firewall, VPN"
]
create_mario_banner(portfolio_lines, "info_portfolio.png", font_size=16, text_color="#FFFFFF", bg_color="#000000", width=800)

portfolio_warn = ["WARNING: Most repos are PRIVATE", "Contains: Production APIs, internal tooling"]
create_mario_banner(portfolio_warn, "info_portfolio_warn.png", font_size=12, text_color="#FFFFFF", bg_color="#E8003D", width=750, height=60)

# Intro & Footer
intro_lines = ["It's-a me, Wissa!", "Player 1 has entered!", "Press START to collaborate!"]
create_mario_banner(intro_lines, "intro.png", font_size=16, text_color="#FBD000", bg_color="#E8003D", width=700)

create_mario_banner(["> sudo make it work", "INSERT COIN"], "footer_sudo.png", font_size=18, text_color="#FFFFFF", bg_color="#000000", width=600)

# Small labels
create_mario_banner(["PLAYER 1"], "player1.png", font_size=12, text_color="#FBD000", bg_color="#E8003D", border_width=4, padding=10, width=150)
