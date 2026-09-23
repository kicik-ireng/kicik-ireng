import os
from PIL import Image

def make_bobbing_gif(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Skipping {input_path}, not found.")
        return
        
    img = Image.open(input_path).convert("RGBA")
    
    # Remove white background
    datas = img.getdata()
    new_data = []
    for item in datas:
        # if almost white, make transparent
        if item[0] > 230 and item[1] > 230 and item[2] > 230:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    img.putdata(new_data)
    
    # Create frames (bobbing up and down)
    width, height = img.size
    frame1 = Image.new("RGBA", (width, height + 6), (255,255,255,0))
    frame1.paste(img, (0, 6), img)
    
    frame2 = Image.new("RGBA", (width, height + 6), (255,255,255,0))
    frame2.paste(img, (0, 0), img)
    
    # Save as GIF
    # PIL GIF saving requires specific modes sometimes, but RGBA works if we use transparency
    # We will convert to P mode for GIF
    f1_p = frame1.convert("P", dither=None)
    f2_p = frame2.convert("P", dither=None)
    
    f1_p.save(output_path, save_all=True, append_images=[f2_p], duration=250, loop=0, transparency=255, disposal=2)
    print(f"Generated {output_path}")

make_bobbing_gif("assets/mario_mushroom.jpg", "assets/anim_mushroom.gif")
make_bobbing_gif("assets/mario_star.jpg", "assets/anim_star.gif")
make_bobbing_gif("assets/mario_coin.jpg", "assets/anim_coin.gif")
make_bobbing_gif("assets/mario_jumping.jpg", "assets/anim_mario.gif")
