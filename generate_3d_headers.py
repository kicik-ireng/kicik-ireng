import os
from PIL import Image, ImageDraw, ImageFont

font_path = "Anton-Regular.ttf"

def create_3d_text(text, filename, font_size=120, top_color="#00f2fe", depth_3d=20, color_3d="#0a2a43", width=800, height=300):
    img = Image.new('RGBA', (width, height), (0,0,0,0))
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    
    bbox = d.textbbox((0,0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    start_x = (width - text_width) / 2
    start_y = (height - text_height) / 2 - depth_3d/2
    
    # 3D extrusion
    for i in range(depth_3d, 0, -1):
        shade = max(0, int(20 - i*0.5))
        current_3d_color = (10+shade, 30+shade, 60+shade, 255)
        d.text((start_x - i, start_y + i), text, fill=current_3d_color, font=font)
        
    d.text((start_x, start_y), text, fill=top_color, font=font)
    
    img.save(os.path.join('assets', filename))

# Sections
create_3d_text("MY SKILL SET", "3d_head_skills.png", font_size=80, top_color="#fbd000", depth_3d=15, width=600, height=150)
create_3d_text("CONNECT WITH ME", "3d_head_connect.png", font_size=80, top_color="#fbd000", depth_3d=15, width=700, height=150)
create_3d_text("CURRENTLY BUILDING", "3d_head_building.png", font_size=80, top_color="#fbd000", depth_3d=15, width=800, height=150)
