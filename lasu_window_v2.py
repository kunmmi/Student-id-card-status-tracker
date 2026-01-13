#!/usr/bin/env python3
"""
University of Ibadan ID Card Tracker - Standalone Window Application V2
Uses subprocess for Flask instead of threading
"""

import sys
import os
import time
import subprocess
import signal
from pathlib import Path

# Try to import PyQt5
try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
    from PyQt5.QtCore import QUrl, Qt
    from PyQt5.QtGui import QIcon
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    HAS_PYQT5 = True
except ImportError as e:
    print(f"❌ PyQt5 not available: {e}")
    print("Install with: pip install PyQt5 PyQtWebEngine")
    sys.exit(1)

class University of IbadanMainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        self.flask_process = None
        self.setup_ui()
        self.start_flask_server()
        
    def setup_ui(self):
        """Set up the user interface"""
        self.setWindowTitle("University of Ibadan ID Card Tracker")
        self.setGeometry(100, 100, 1200, 800)
        self.setMinimumSize(800, 600)
        
        # Set window icon if available
        icon_path = Path("id_card_tracker.ico")
        if icon_path.exists():
            try:
                self.setWindowIcon(QIcon(str(icon_path)))
            except:
                pass
        
        # Create web view
        print("✅ Creating web view...")
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        
        # Add status bar
        self.statusBar().showMessage("Initializing University of Ibadan ID Card Tracker...")
        
    def start_flask_server(self):
        """Start Flask server as subprocess"""
        def start():
            print("🚀 Starting Flask server as subprocess...")
            try:
                # Run Flask in a subprocess
                self.flask_process = subprocess.Popen(
                    [sys.executable, "app.py"],
                    creationflags=subprocess.CREATE_NO_WINDOW,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                print("✅ Flask process started")
                
                # Wait for Flask to be ready
                time.sleep(3)
                
                # Load the page
                url = QUrl("http://localhost:5000")
                print("✅ Loading URL in browser...")
                self.browser.setUrl(url)
                self.statusBar().showMessage("✅ University of Ibadan ID Card Tracker Ready - http://localhost:5000")
                
                # Show welcome message
                msg = QMessageBox(self)
                msg.setWindowTitle("University of Ibadan ID Card Tracker")
                msg.setText("Welcome to University of Ibadan ID Card Tracker!")
                msg.setInformativeText(
                    "Application is ready to use.\n\n"
                    "Admin Login:\n"
                    "Username: admin\n"
                    "Password: admin123"
                )
                msg.exec_()
            except Exception as e:
                print(f"❌ Error: {e}")
                import traceback
                traceback.print_exc()
                
        import threading
        flask_thread = threading.Thread(target=start, daemon=True)
        flask_thread.start()
    
    def closeEvent(self, event):
        """Handle window close event"""
        reply = QMessageBox.question(
            self,
            'Exit Application',
            'Are you sure you want to close the University of Ibadan ID Card Tracker?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # Kill Flask process
            if self.flask_process:
                try:
                    self.flask_process.terminate()
                    print("✅ Flask server stopped")
                except:
                    pass
            event.accept()
            print("\n👋 University of Ibadan ID Card Tracker closed.")
        else:
            event.ignore()

def main():
    """Main entry point"""
    print("=" * 60)
    print("🎓 University of Ibadan ID Card Tracker - Standalone Window V2")
    print("=" * 60)
    print("🚀 Starting application...")
    print("🔑 Admin login: username='admin', password='admin123'")
    print("=" * 60)
    
    app = QApplication(sys.argv)
    app.setApplicationName("University of Ibadan ID Card Tracker")
    
    window = University of IbadanMainWindow()
    window.show()
    
    print("✅ Window should now be visible...")
    
    result = app.exec_()
    
    print(f"⚠️ Event loop exited with code: {result}")
    return result

if __name__ == '__main__':
    sys.exit(main())

