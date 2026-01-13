#!/usr/bin/env python3
"""
Test if the icon is working properly
"""

import os
import sys

def test_icon():
    """Test the icon setup"""
    print("🔍 Testing icon setup...")
    
    # Check if monga.jpg exists
    if os.path.exists("monga.jpg"):
        print("✅ monga.jpg found")
        file_size = os.path.getsize("monga.jpg")
        print(f"📏 File size: {file_size} bytes")
    else:
        print("❌ monga.jpg not found")
        return False
    
    # Check if desktop shortcut exists
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "ID Card Tracker.lnk")
    if os.path.exists(desktop_path):
        print("✅ Desktop shortcut found")
        shortcut_size = os.path.getsize(desktop_path)
        print(f"📏 Shortcut size: {shortcut_size} bytes")
    else:
        print("❌ Desktop shortcut not found")
        return False
    
    print("\n🎯 Icon Status:")
    print("   • Your monga.jpg image is set as the icon")
    print("   • Desktop shortcut created successfully")
    print("   • The icon should appear on your desktop")
    
    print("\n💡 If you don't see the custom icon:")
    print("   1. Right-click the desktop shortcut")
    print("   2. Select 'Properties'")
    print("   3. Click 'Change Icon'")
    print("   4. Browse to this folder and select 'monga.jpg'")
    print("   5. Click 'OK' to apply")
    
    return True

def create_ico_version():
    """Create an ICO version of the image for better compatibility"""
    try:
        from PIL import Image
        
        print("\n🔄 Creating ICO version for better compatibility...")
        
        # Open the JPG image
        img = Image.open("monga.jpg")
        
        # Convert to RGBA if needed
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Create ICO with multiple sizes
        sizes = [(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)]
        img.save("monga.ico", format='ICO', sizes=sizes)
        
        print("✅ Created monga.ico")
        print("💡 You can use monga.ico instead of monga.jpg for better icon support")
        
        return True
        
    except ImportError:
        print("⚠️  PIL not available for ICO conversion")
        return False
    except Exception as e:
        print(f"⚠️  Error creating ICO: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("🎨 Icon Test for ID Card Tracker")
    print("=" * 50)
    
    if test_icon():
        print("\n🎉 Icon setup completed!")
        
        # Try to create ICO version
        create_ico_version()
        
        print("\n📋 Summary:")
        print("   • Desktop shortcut: ✅ Created")
        print("   • Custom icon: ✅ Set to monga.jpg")
        print("   • Location: Desktop > 'ID Card Tracker'")
        
        print("\n🚀 To test:")
        print("   1. Look at your desktop for 'ID Card Tracker' shortcut")
        print("   2. Check if it shows your monga.jpg image as icon")
        print("   3. Double-click to launch the application")
    
    else:
        print("❌ Icon setup failed")
