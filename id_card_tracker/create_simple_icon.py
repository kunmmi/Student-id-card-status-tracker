#!/usr/bin/env python3
"""
Create a simple icon for the ID Card Tracker
"""

import os

def create_icon_file():
    """Create a simple icon file"""
    
    # Create a simple icon using base64 encoded ICO data
    # This is a minimal 16x16 blue square icon
    icon_data = b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x20\x00\x68\x04\x00\x00\x16\x00\x00\x00\x28\x00\x00\x00\x10\x00\x00\x00\x20\x00\x00\x00\x01\x00\x20\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    
    # Add more icon data to make it a proper ICO file
    # This creates a simple blue square icon
    full_icon_data = (
        b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x20\x00\x68\x04\x00\x00\x16\x00\x00\x00'
        b'\x28\x00\x00\x00\x10\x00\x00\x00\x20\x00\x00\x00\x01\x00\x20\x00\x00\x00\x00\x00\x00\x04'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        # Add a simple blue square pattern
        b'\x1E\x3A\x8A\xFF' * 64  # Blue color repeated for 16x16 pixels
    )
    
    with open("id_card_tracker.ico", "wb") as f:
        f.write(full_icon_data)
    
    print("✅ Simple icon created: id_card_tracker.ico")
    return "id_card_tracker.ico"

def create_alternative_icon():
    """Create an alternative icon using a different method"""
    
    # Create a simple text file that can be used as icon reference
    icon_info = """ID Card Tracker Icon
==================
This is a placeholder for the ID Card Tracker icon.
The installer will use a default Windows icon if this file is not found.
"""
    
    with open("icon_info.txt", "w") as f:
        f.write(icon_info)
    
    print("✅ Icon info file created: icon_info.txt")
    return "icon_info.txt"

if __name__ == "__main__":
    print("🎨 Creating icon for ID Card Tracker...")
    
    try:
        icon_path = create_icon_file()
        print(f"🎯 Icon created: {icon_path}")
    except Exception as e:
        print(f"⚠️  Error creating icon: {e}")
        create_alternative_icon()
    
    print("📌 The installer will use this icon for the desktop shortcut!")
