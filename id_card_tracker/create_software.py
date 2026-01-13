#!/usr/bin/env python3
"""
Simple script to create a standalone executable
"""

import subprocess
import sys
import os

def main():
    print("🔨 Creating ID Card Tracker Software")
    print("=" * 50)
    
    # Install PyInstaller
    print("📦 Installing PyInstaller...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # Create the executable
    print("🔨 Building executable...")
    cmd = [
        "pyinstaller",
        "--onefile",
        "--name=ID_Card_Tracker",
        "standalone_app.py"
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("✅ Build successful!")
        
        # Create launcher
        launcher = '''@echo off
title ID Card Tracker
echo ========================================
echo    University of Ibadan
echo    ID Card Tracker
echo ========================================
echo.
echo Starting application...
echo The app will open in your web browser.
echo.
dist\\ID_Card_Tracker.exe
echo.
echo Application closed.
pause
'''
        
        with open("Launch_ID_Card_Tracker.bat", "w") as f:
            f.write(launcher)
        
        print("📁 Files created:")
        print("   dist/ID_Card_Tracker.exe - Main executable")
        print("   Launch_ID_Card_Tracker.bat - Easy launcher")
        print("\n🚀 To distribute:")
        print("   1. Copy the 'dist' folder")
        print("   2. Copy 'Launch_ID_Card_Tracker.bat'")
        print("   3. Users double-click the .bat file to run")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        print("\nAlternative: You can still run the web app with:")
        print("   python standalone_app.py")

if __name__ == "__main__":
    main()
