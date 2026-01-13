#!/usr/bin/env python3
"""
Script to build the ID Card Tracker as a standalone executable
"""

import subprocess
import sys
import os

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("PyInstaller is already installed")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building standalone executable...")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",  # Create a single executable file
        "--windowed",  # Hide console window (for Windows)
        "--name=ID_Card_Tracker",  # Name of the executable
        "--add-data=templates;templates",  # Include templates folder
        "--add-data=static;static",  # Include static files
        "--hidden-import=flask",
        "--hidden-import=werkzeug",
        "simple_app.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print("\n✅ Build successful!")
        print("📁 Executable created in: dist/ID_Card_Tracker.exe")
        print("\n🚀 You can now distribute this .exe file to users!")
        print("   Users can run it without installing Python.")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False
    
    return True

def create_launcher_script():
    """Create a simple launcher script for easier distribution"""
    launcher_content = '''@echo off
echo Starting ID Card Tracker...
echo.
echo The application will open in your web browser.
echo If it doesn't open automatically, go to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server.
echo.
ID_Card_Tracker.exe
pause
'''
    
    with open("launch_tracker.bat", "w") as f:
        f.write(launcher_content)
    
    print("📄 Created launcher script: launch_tracker.bat")

if __name__ == "__main__":
    print("🔨 Building ID Card Tracker as Standalone Software")
    print("=" * 50)
    
    # Install PyInstaller
    install_pyinstaller()
    
    # Build executable
    if build_executable():
        # Create launcher script
        create_launcher_script()
        
        print("\n🎉 Build Complete!")
        print("\nFiles created:")
        print("  📦 dist/ID_Card_Tracker.exe - Main executable")
        print("  🚀 launch_tracker.bat - Easy launcher")
        print("\nTo distribute:")
        print("  1. Copy the entire 'dist' folder")
        print("  2. Or just copy 'ID_Card_Tracker.exe' and 'launch_tracker.bat'")
        print("  3. Users can double-click 'launch_tracker.bat' to run")
    else:
        print("\n❌ Build failed. Please check the error messages above.")
