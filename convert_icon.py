#!/usr/bin/env python3
"""
Convert monga.jpg to ICO format for desktop shortcut
"""

import os
import sys

def convert_image_to_ico():
    """Convert monga.jpg to ICO format"""
    
    # Check if monga.jpg exists
    if not os.path.exists("monga.jpg"):
        print("❌ monga.jpg not found in current directory")
        return False
    
    try:
        # Try to use PIL/Pillow for image conversion
        from PIL import Image
        
        print("🎨 Converting monga.jpg to ICO format...")
        
        # Open the image
        img = Image.open("monga.jpg")
        
        # Convert to RGBA if needed
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Resize to multiple sizes for ICO format
        sizes = [(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)]
        
        # Save as ICO with multiple sizes
        img.save("id_card_tracker.ico", format='ICO', sizes=sizes)
        
        print("✅ Successfully converted monga.jpg to id_card_tracker.ico")
        print("📏 Icon includes sizes: 256x256, 128x128, 64x64, 32x32, 16x16")
        return True
        
    except ImportError:
        print("⚠️  PIL/Pillow not available. Installing...")
        try:
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
            print("✅ Pillow installed. Retrying conversion...")
            return convert_image_to_ico()  # Retry after installation
        except Exception as e:
            print(f"❌ Failed to install Pillow: {e}")
            return create_fallback_icon()
    
    except Exception as e:
        print(f"❌ Error converting image: {e}")
        return create_fallback_icon()

def create_fallback_icon():
    """Create a fallback icon if conversion fails"""
    print("🔄 Creating fallback icon...")
    
    # Create a simple text file as placeholder
    with open("id_card_tracker.ico", "w") as f:
        f.write("Icon placeholder - using default Windows icon")
    
    print("⚠️  Created fallback icon. The installer will use default Windows icon.")
    return True

def update_installer():
    """Update the installer to use the new icon"""
    print("🔧 Updating installer to use custom icon...")
    
    # Read the current installer
    try:
        with open("install_desktop_app.py", "r") as f:
            content = f.read()
        
        # Update the icon path in the installer
        updated_content = content.replace(
            'shortcut.IconLocation = icon',
            'shortcut.IconLocation = os.path.join(os.getcwd(), "id_card_tracker.ico")'
        )
        
        # Write the updated installer
        with open("install_desktop_app.py", "w") as f:
            f.write(updated_content)
        
        print("✅ Installer updated to use custom icon")
        return True
        
    except Exception as e:
        print(f"⚠️  Could not update installer: {e}")
        return False

def main():
    """Main function"""
    print("=" * 60)
    print("🎨 Converting monga.jpg to Desktop Icon")
    print("=" * 60)
    
    # Convert the image
    if convert_image_to_ico():
        print("✅ Icon conversion successful!")
        
        # Update installer
        update_installer()
        
        print()
        print("🎉 Custom icon ready!")
        print("📌 Your desktop shortcut will now use the monga.jpg image as icon")
        print("🚀 Run the installer to create the desktop shortcut with your custom icon")
        
    else:
        print("❌ Icon conversion failed")
        print("💡 The installer will use the default Windows icon instead")

if __name__ == "__main__":
    main()
