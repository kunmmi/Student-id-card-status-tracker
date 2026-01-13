#!/usr/bin/env python3
"""
University of Ibadan ID Card Tracker - Desktop Application
This creates a standalone desktop app with its own window
"""

import tkinter as tk
from tkinter import messagebox
import threading
import webbrowser
import time
import sys
import os

# Import Flask app from main app.py
from app import app as flask_app
from models.database import db, Student, Admin

class DesktopApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("University of Ibadan ID Card Tracker")
        self.root.geometry("1200x800")
        self.root.minsize(800, 600)
        
        # Configure window icon if available
        try:
            if os.path.exists("id_card_tracker.ico"):
                self.root.iconbitmap("id_card_tracker.ico")
        except:
            pass
        
        # Start Flask in background thread
        self.start_flask_server()
        
        # Wait a bit for Flask to start
        time.sleep(2)
        
        # Open embedded browser
        self.open_in_window()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def start_flask_server(self):
        """Start Flask server in background thread"""
        def run_flask():
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
            
            flask_app.run(debug=False, host='127.0.0.1', port=5000, use_reloader=False, threaded=True)
        
        flask_thread = threading.Thread(target=run_flask, daemon=True)
        flask_thread.start()
    
    def open_in_window(self):
        """Open the app in the system's default web browser"""
        url = "http://localhost:5000"
        
        # Open in browser (this still uses system browser)
        webbrowser.open(url)
        
        # Show message
        self.show_info()
    
    def show_info(self):
        """Show information dialog"""
        info = "University of Ibadan ID Card Tracker is now running!\n\n"
        info += "The application has opened in your browser.\n"
        info += "If you prefer to use it in a standalone window,\n"
        info += "you can install PyQt or use the web version.\n\n"
        info += "Admin Login:\n"
        info += "Username: admin\n"
        info += "Password: admin123"
        
        messagebox.showinfo("University of Ibadan ID Card Tracker", info)
    
    def on_closing(self):
        """Handle window closing"""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
    
    def run(self):
        """Run the application"""
        self.root.mainloop()

if __name__ == '__main__':
    print("=" * 60)
    print("🎓 University of Ibadan ID Card Tracker - Desktop Application")
    print("=" * 60)
    print("🚀 Starting application...")
    print("🌐 Opening in your default web browser")
    print("🔑 Admin login: username='admin', password='admin123'")
    print("=" * 60)
    
    app = DesktopApp()
    app.run()

