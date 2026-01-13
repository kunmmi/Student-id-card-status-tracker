#!/usr/bin/env python3
"""
University of Ibadan ID Card Tracker - Standalone Window Application
Creates a dedicated window (not using system browser)
"""

import sys
import os
import threading
import time
from pathlib import Path

# Try to import PyQt5
try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
    from PyQt5.QtCore import QUrl, QSize, Qt
    from PyQt5.QtGui import QIcon
    print("✅ PyQt5 core imported successfully")
    HAS_PYQT5 = True
except ImportError as e:
    HAS_PYQT5 = False
    print("⚠️  PyQt5 not installed. Installing required packages...")
    print("Run: pip install PyQt5 PyQtWebEngine")
    sys.exit(1)

# Try to import QWebEngineWidgets separately
try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    HAS_WEBENGINE = True
    print("✅ QWebEngineView imported successfully")
except ImportError as e:
    HAS_WEBENGINE = False
    print(f"⚠️  QWebEngineView not available: {e}")
    print("Web browser embedding will not work without PyQtWebEngine")

# Import Flask app from main app.py
# Only import after PyQt5 is confirmed
try:
    from app import app as flask_app
    from models.database import db, Student, Admin
    FLASK_IMPORTED = True
except Exception as e:
    print(f"⚠️ Warning importing Flask app: {e}")
    FLASK_IMPORTED = False
    flask_app = None
    db = None
    Student = None
    Admin = None

class University of IbadanMainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        
        self.flask_running = False
        self.flask_thread = None
        self.setup_ui()
        
        # Start Flask in a way that doesn't interfere with Qt
        print("🔄 Setting up Flask...")
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
        
        # Create web view (check if QWebEngineView is available)
        if HAS_WEBENGINE:
            from PyQt5.QtWebEngineWidgets import QWebEngineView
            self.browser = QWebEngineView()
            self.setCentralWidget(self.browser)
            print("✅ Web view created")
        else:
            # Fallback: Show a message label
            from PyQt5.QtWidgets import QLabel
            label = QLabel(
                "University of Ibadan ID Card Tracker\n\n"
                "PyQtWebEngine is not fully installed.\n\n"
                "The application will open in your web browser.\n\n"
                "Click OK to continue..."
            )
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size: 14px; padding: 20px;")
            self.setCentralWidget(label)
            print("⚠️ WebEngine not available, showing fallback UI")
            self.browser = None
            
        # Add status bar
        self.statusBar().showMessage("Initializing University of Ibadan ID Card Tracker...")
        
    def start_flask_server(self):
        """Start Flask server in background thread"""
        def run_flask():
            if not FLASK_IMPORTED:
                print("❌ Flask app not imported, cannot start server")
                return
                
            try:
                # Wait a moment for the UI to be ready
                time.sleep(1)
                
                print("🔧 Initializing database...")
                # Initialize database
                with flask_app.app_context():
                    db.create_all()
                    
                    # Create default admin if not exists
                    if not Admin.query.first():
                        from werkzeug.security import generate_password_hash
                        default_admin = Admin(
                            username='admin',
                            password=generate_password_hash('admin123')
                        )
                        db.session.add(default_admin)
                        db.session.commit()
                        print("✅ Default admin user created!")
                
                print("🚀 Starting Flask server...")
                # Run Flask server
                self.flask_running = True
                try:
                    flask_app.run(debug=False, host='127.0.0.1', port=5000, use_reloader=False, threaded=True)
                except Exception as e:
                    print(f"❌ Flask server error: {e}")
                    import traceback
                    traceback.print_exc()
            except Exception as e:
                print(f"❌ Error starting Flask server: {e}")
                import traceback
                traceback.print_exc()
        
        # Start Flask in separate thread
        self.flask_thread = threading.Thread(target=run_flask, daemon=True)
        self.flask_thread.start()
        print("✅ Flask thread started")
        
        # Wait for Flask to be ready, then load the page
        def load_page():
            try:
                # Wait longer for Flask to start
                print("⏳ Waiting for Flask server to start...")
                time.sleep(3)
                
                # Check if Flask is running
                import socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex(('127.0.0.1', 5000))
                sock.close()
                
                if result == 0:
                    print("✅ Flask server is running!")
                    url = "http://localhost:5000"
                    
                    if self.browser:
                        # Load in embedded browser
                        self.browser.setUrl(QUrl(url))
                        self.statusBar().showMessage("✅ University of Ibadan ID Card Tracker Ready - http://localhost:5000")
                        print("✅ Page loaded in embedded browser")
                    else:
                        # Fallback: open in system browser and keep window open
                        import webbrowser
                        webbrowser.open(url)
                        self.statusBar().showMessage("✅ University of Ibadan ID Card Tracker ready - opened in browser")
                        print("✅ Opened in system browser")
                    
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
                else:
                    print("⚠️ Flask server not responding yet")
                    # Flask not ready yet, wait more
                    time.sleep(2)
                    url = "http://localhost:5000"
                    if self.browser:
                        self.browser.setUrl(QUrl(url))
                        self.statusBar().showMessage("✅ University of Ibadan ID Card Tracker Ready")
                    else:
                        import webbrowser
                        webbrowser.open(url)
                        self.statusBar().showMessage("✅ University of Ibadan ID Card Tracker ready")
            except Exception as e:
                print(f"❌ Error loading page: {e}")
                import traceback
                traceback.print_exc()
                self.statusBar().showMessage(f"❌ Error: {e}")
        
        load_thread = threading.Thread(target=load_page, daemon=True)
        load_thread.start()
    
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
            # Try to properly shutdown Flask
            try:
                from werkzeug.serving import make_server
                import signal
                # Signal the Flask thread to stop
                self.flask_running = False
            except:
                pass
            event.accept()
            print("\n👋 University of Ibadan ID Card Tracker closed. Thank you for using the application!")
        else:
            event.ignore()

def main():
    """Main entry point"""
    if not HAS_PYQT5:
        print("\n❌ PyQt5 and PyQtWebEngine are required!")
        print("Install them with:")
        print("  pip install PyQt5 PyQtWebEngine")
        return 1
    
    print("=" * 60)
    print("🎓 University of Ibadan ID Card Tracker - Standalone Window")
    print("=" * 60)
    print("🚀 Starting application in dedicated window...")
    print("🔑 Admin login: username='admin', password='admin123'")
    print("=" * 60)
    
    try:
        # Create Qt application
        print("📱 Creating QApplication...")
        app = QApplication(sys.argv)
        app.setApplicationName("University of Ibadan ID Card Tracker")
        print("✅ QApplication created")
        
        # Create and show main window
        print("📱 Creating window...")
        window = University of IbadanMainWindow()
        print("✅ Window created successfully")
        
        print("🔍 Showing window...")
        window.show()
        print("✅ Window is now visible")
        
        # Keep the window alive
        window.raise_()
        window.activateWindow()
        print("✅ Window activated")
        
        print("🔄 Starting event loop...")
        print("✅ Window should remain open now...")
        # Run the event loop
        result = app.exec_()
        print(f"⚠️ Event loop returned: {result}")
        sys.exit(result)
    except Exception as e:
        print(f"❌ Critical error: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")
        return 1

if __name__ == '__main__':
    sys.exit(main())

