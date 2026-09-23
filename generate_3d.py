import os
import urllib.request
from PIL import Image, ImageDraw, ImageFont, ImageFilter

font_url = "https://github.com/google/fonts/raw/main/ofl/anton/Anton-Regular.ttf"
font_path = "Anton-Regular.ttf"

if not os.path.exists(font_path):
    try:
        urllib.request.urlretrieve(font_url, font_path)
    except Exception as e:
        print(f"Failed to download font: {e}")

def create_3d_text(text, filename, font_size=120, top_color="#00f2fe", bottom_color="#4facfe", depth_3d=20, color_3d="#0a2a43", width=800, height=300):
    img = Image.new('RGBA', (width, height), (0,0,0,0))
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    
    # Get text size
    bbox = d.textbbox((0,0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    start_x = (width - text_width) / 2
    start_y = (height - text_height) / 2 - depth_3d/2
    
    # Draw 3D extrusion (bottom layers)
    for i in range(depth_3d, 0, -1):
        # We can add a slight gradient or darkening to the extrusion
        shade = max(0, int(20 - i*0.5))
        current_3d_color = (10+shade, 30+shade, 60+shade, 255)
        d.text((start_x - i, start_y + i), text, fill=current_3d_color, font=font)
        
    # Draw top layer
    d.text((start_x, start_y), text, fill=top_color, font=font)
    
    os.makedirs('assets', exist_ok=True)
    img.save(os.path.join('assets', filename))
    print(f"Generated {filename}")

create_3d_text("WISSA GAMMA", "3d_name.png", font_size=110, top_color="#00f2fe", depth_3d=25)
create_3d_text("FULLSTACK DEVELOPER", "3d_title.png", font_size=70, top_color="#fbd000", depth_3d=15, color_3d="#b32400")
