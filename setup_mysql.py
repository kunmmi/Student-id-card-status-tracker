#!/usr/bin/env python3
"""
MySQL Setup Script for ID Card Tracker
This script helps you set up MySQL connection and test it
"""

import os
import sys

def test_mysql_connection():
    """Test MySQL connection with user-provided credentials"""
    print("=" * 60)
    print("MySQL Connection Test")
    print("=" * 60)
    print()
    
    # Get credentials from user
    host = input("MySQL Host (default: localhost): ").strip() or "localhost"
    port = input("MySQL Port (default: 3306): ").strip() or "3306"
    user = input("MySQL Username: ").strip()
    password = input("MySQL Password: ").strip()
    database = input("Database Name (default: id_card_tracker): ").strip() or "id_card_tracker"
    
    print()
    print("Testing connection...")
    
    try:
        import pymysql
        
        connection = pymysql.connect(
            host=host,
            port=int(port),
            user=user,
            password=password,
            database=database,
            charset='utf8mb4'
        )
        
        print("✅ MySQL connection successful!")
        connection.close()
        
        # Create .env file
        print()
        print("Creating .env file with your credentials...")
        
        env_content = f"""# Database Configuration
DB_TYPE=mysql
DB_HOST={host}
DB_PORT={port}
DB_USER={user}
DB_PASSWORD={password}
DB_NAME={database}

# Secret Key for Flask sessions
SECRET_KEY=your-secret-key-change-this-in-production
"""
        
        with open('.env', 'w') as f:
            f.write(env_content)
        
        print("✅ .env file created successfully!")
        print()
        print("You can now run the application with: python app.py")
        print("The app will automatically use MySQL!")
        
        return True
        
    except ImportError:
        print("❌ PyMySQL not installed!")
        print("Install it with: pip install PyMySQL")
        return False
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print()
        print("Please check:")
        print("1. MySQL server is running")
        print("2. Database exists (CREATE DATABASE id_card_tracker)")
        print("3. User has proper permissions")
        print("4. Credentials are correct")
        return False

if __name__ == '__main__':
    if test_mysql_connection():
        print()
        print("=" * 60)
        print("Setup Complete!")
        print("=" * 60)
    else:
        print()
        print("=" * 60)
        print("Setup Failed - Please fix the errors above")
        print("=" * 60)
        sys.exit(1)

