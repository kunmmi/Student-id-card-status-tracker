#!/usr/bin/env python3
"""Simple test to check if PyQt window stays open"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Window")
        self.setGeometry(100, 100, 500, 300)
        
        label = QLabel("If you can see this, the window is working!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TestWindow()
    window.show()
    print("✅ Window should be visible now. Close it to exit.")
    sys.exit(app.exec_())

