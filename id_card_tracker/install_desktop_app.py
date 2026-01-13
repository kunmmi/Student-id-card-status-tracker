#!/usr/bin/env python3
"""
ID Card Tracker - Desktop Application Installer
This script installs the ID Card Tracker as a desktop application
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing required dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "pywin32", "winshell"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def create_desktop_shortcut():
    """Create desktop shortcut"""
    try:
        import winshell
        from win32com.client import Dispatch
        
        desktop = winshell.desktop()
        path = os.path.join(desktop, "ID Card Tracker.lnk")
        target = os.path.join(os.getcwd(), "desktop_app.py")
        wDir = os.getcwd()
        
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = sys.executable
        shortcut.Arguments = f'"{target}"'
        shortcut.WorkingDirectory = wDir
        shortcut.Description = "University of Ibadan - ID Card Tracker"
        shortcut.IconLocation = os.path.join(os.getcwd(), "monga.ico")
        shortcut.save()
        
        print("✅ Desktop shortcut created successfully!")
        return True
    except ImportError:
        print("⚠️  Could not create desktop shortcut (missing pywin32)")
        return False
    except Exception as e:
        print(f"⚠️  Could not create desktop shortcut: {e}")
        return False

def create_start_menu_shortcut():
    """Create start menu shortcut"""
    try:
        import winshell
        from win32com.client import Dispatch
        
        start_menu = winshell.start_menu()
        programs_folder = os.path.join(start_menu, "Programs")
        
        # Create ID Card Tracker folder in Programs
        app_folder = os.path.join(programs_folder, "ID Card Tracker")
        os.makedirs(app_folder, exist_ok=True)
        
        # Create shortcut
        path = os.path.join(app_folder, "ID Card Tracker.lnk")
        target = os.path.join(os.getcwd(), "desktop_app.py")
        wDir = os.getcwd()
        
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = sys.executable
        shortcut.Arguments = f'"{target}"'
        shortcut.WorkingDirectory = wDir
        shortcut.Description = "University of Ibadan - ID Card Tracker"
        shortcut.IconLocation = os.path.join(os.getcwd(), "monga.ico")
        shortcut.save()
        
        print("✅ Start menu shortcut created successfully!")
        return True
    except Exception as e:
        print(f"⚠️  Could not create start menu shortcut: {e}")
        return False

def create_uninstaller():
    """Create uninstaller script"""
    uninstaller_content = '''@echo off
echo Uninstalling ID Card Tracker...
echo.

REM Remove desktop shortcut
if exist "%USERPROFILE%\\Desktop\\ID Card Tracker.lnk" (
    del "%USERPROFILE%\\Desktop\\ID Card Tracker.lnk"
    echo Desktop shortcut removed.
)

REM Remove start menu shortcut
if exist "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\ID Card Tracker" (
    rmdir /s /q "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\ID Card Tracker"
    echo Start menu shortcut removed.
)

echo.
echo ID Card Tracker has been uninstalled.
echo Note: Application files are still in the installation folder.
echo You can delete the entire folder if you want to remove everything.
echo.
pause
'''
    
    with open("uninstall.bat", "w") as f:
        f.write(uninstaller_content)
    
    print("✅ Uninstaller created: uninstall.bat")

def main():
    """Main installation function"""
    print("=" * 60)
    print("🎓 University of Ibadan - ID Card Tracker")
    print("📦 Desktop Application Installer")
    print("=" * 60)
    print()
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Installation failed. Please check the error messages above.")
        return
    
    print()
    
    # Create shortcuts
    print("📌 Creating shortcuts...")
    create_desktop_shortcut()
    create_start_menu_shortcut()
    
    print()
    
    # Create uninstaller
    print("🗑️  Creating uninstaller...")
    create_uninstaller()
    
    print()
    print("=" * 60)
    print("🎉 Installation Complete!")
    print("=" * 60)
    print()
    print("✅ ID Card Tracker has been installed as a desktop application!")
    print()
    print("📋 What was installed:")
    print("   • Desktop shortcut: 'ID Card Tracker' on your desktop")
    print("   • Start menu shortcut: Start Menu > Programs > ID Card Tracker")
    print("   • Uninstaller: uninstall.bat (in this folder)")
    print()
    print("🚀 How to use:")
    print("   1. Double-click the desktop shortcut 'ID Card Tracker'")
    print("   2. Or find it in Start Menu > Programs > ID Card Tracker")
    print("   3. The app will start and open in your web browser")
    print()
    print("🔑 Admin login: username='admin', password='admin123'")
    print()
    print("💡 The application will run on http://localhost:5000")
    print("   You can bookmark this URL for quick access.")
    print()
    
    # Ask if user wants to launch the app now
    try:
        launch = input("🚀 Would you like to launch the application now? (y/n): ").lower().strip()
        if launch in ['y', 'yes']:
            print("🚀 Launching ID Card Tracker...")
            subprocess.Popen([sys.executable, "desktop_app.py"])
    except KeyboardInterrupt:
        print("\n👋 Installation complete. You can launch the app anytime using the shortcuts!")

if __name__ == "__main__":
    main()
