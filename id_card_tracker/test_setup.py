#!/usr/bin/env python3
"""
Test script to verify the ID Card Tracker application setup
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import flask
        print("✓ Flask imported successfully")
    except ImportError as e:
        print(f"✗ Flask import failed: {e}")
        return False
    
    try:
        import pandas
        print("✓ Pandas imported successfully")
    except ImportError as e:
        print(f"✗ Pandas import failed: {e}")
        return False
    
    try:
        import openpyxl
        print("✓ OpenPyXL imported successfully")
    except ImportError as e:
        print(f"✗ OpenPyXL import failed: {e}")
        return False
    
    return True

def test_database_models():
    """Test if database models can be imported"""
    print("\nTesting database models...")
    
    try:
        from models.database import Student, Admin
        print("✓ Database models imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Database models import failed: {e}")
        return False

def test_flask_app():
    """Test if Flask app can be created"""
    print("\nTesting Flask app creation...")
    
    try:
        from app import app
        print("✓ Flask app created successfully")
        return True
    except Exception as e:
        print(f"✗ Flask app creation failed: {e}")
        return False

def test_file_structure():
    """Test if all required files exist"""
    print("\nTesting file structure...")
    
    required_files = [
        'app.py',
        'requirements.txt',
        'models/__init__.py',
        'models/database.py',
        'templates/base.html',
        'templates/index.html',
        'templates/search.html',
        'templates/search_result.html',
        'templates/admin_login.html',
        'templates/admin_dashboard.html',
        'templates/admin_upload.html',
        'README.md'
    ]
    
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} - MISSING")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\nMissing files: {', '.join(missing_files)}")
        return False
    
    return True

def main():
    """Run all tests"""
    print("ID Card Tracker - Setup Verification")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_database_models,
        test_flask_app,
        test_file_structure
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 40)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your application is ready to run.")
        print("\nTo start the application:")
        print("1. Activate your virtual environment (if using one)")
        print("2. Run: python app.py")
        print("3. Open: http://localhost:5000")
        print("\nDefault admin credentials:")
        print("Username: admin")
        print("Password: admin123")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main()) 