#!/usr/bin/env python3
"""
Create a custom icon for the ID Card Tracker desktop application
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_app_icon():
    """Create a custom icon for the ID Card Tracker"""
    
    # Create a 256x256 image with a blue background
    size = 256
    img = Image.new('RGBA', (size, size), (30, 58, 138, 255))  # Blue background
    draw = ImageDraw.Draw(img)
    
    # Draw a white card shape in the center
    card_width = 120
    card_height = 80
    card_x = (size - card_width) // 2
    card_y = (size - card_height) // 2 - 10
    
    # Card background (white)
    draw.rounded_rectangle(
        [card_x, card_y, card_x + card_width, card_y + card_height],
        radius=8,
        fill=(255, 255, 255, 255)
    )
    
    # Card border
    draw.rounded_rectangle(
        [card_x, card_y, card_x + card_width, card_y + card_height],
        radius=8,
        outline=(0, 0, 0, 255),
        width=2
    )
    
    # Draw ID card elements
    # Photo area (small rectangle)
    photo_size = 20
    photo_x = card_x + 10
    photo_y = card_y + 10
    draw.rectangle(
        [photo_x, photo_y, photo_x + photo_size, photo_y + photo_size],
        fill=(200, 200, 200, 255),
        outline=(0, 0, 0, 255)
    )
    
    # Name line
    draw.line(
        [photo_x + photo_size + 10, photo_y + 8, card_x + card_width - 10, photo_y + 8],
        fill=(0, 0, 0, 255),
        width=2
    )
    
    # Matric number line
    draw.line(
        [photo_x + photo_size + 10, photo_y + 20, card_x + card_width - 10, photo_y + 20],
        fill=(0, 0, 0, 255),
        width=2
    )
    
    # Department line
    draw.line(
        [photo_x + photo_size + 10, photo_y + 32, card_x + card_width - 10, photo_y + 32],
        fill=(0, 0, 0, 255),
        width=2
    )
    
    # Add "UI" text at the bottom
    try:
        # Try to use a system font
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    ui_text = "UI"
    text_bbox = draw.textbbox((0, 0), ui_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = (size - text_width) // 2
    text_y = card_y + card_height + 15
    
    draw.text((text_x, text_y), ui_text, fill=(255, 255, 255, 255), font=font)
    
    # Add "ID CARD" text below
    id_text = "ID CARD"
    try:
        small_font = ImageFont.truetype("arial.ttf", 12)
    except:
        small_font = ImageFont.load_default()
    
    text_bbox = draw.textbbox((0, 0), id_text, font=small_font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = (size - text_width) // 2
    text_y += 20
    
    draw.text((text_x, text_y), id_text, fill=(255, 255, 255, 255), font=small_font)
    
    # Save as ICO file
    ico_path = "id_card_tracker.ico"
    img.save(ico_path, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
    
    print(f"✅ Icon created: {ico_path}")
    return ico_path

def create_simple_icon():
    """Create a simple icon without PIL dependency"""
    # Create a simple text-based icon file
    icon_content = '''[Icon]
ID=1
Name=ID Card Tracker
Description=University of Ibadan ID Card Tracker
'''
    
    with open("app_icon.ico", "w") as f:
        f.write(icon_content)
    
    print("✅ Simple icon placeholder created: app_icon.ico")
    return "app_icon.ico"

if __name__ == "__main__":
    print("🎨 Creating custom icon for ID Card Tracker...")
    
    try:
        # Try to create a proper icon with PIL
        icon_path = create_app_icon()
    except ImportError:
        print("⚠️  PIL not available, creating simple icon...")
        icon_path = create_simple_icon()
    except Exception as e:
        print(f"⚠️  Error creating icon: {e}")
        print("Creating simple icon...")
        icon_path = create_simple_icon()
    
    print(f"🎯 Icon ready: {icon_path}")
    print("📌 This icon will be used for the desktop shortcut!")
