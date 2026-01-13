#!/usr/bin/env python3
"""
Quick MySQL Connection Test
Tests if we can connect to MySQL server
"""

import pymysql

print("=" * 60)
print("MySQL Connection Test")
print("=" * 60)
print()

# Try to connect with default root credentials
# User will need to provide their actual credentials

print("Testing MySQL connection...")
print()
print("Please provide your MySQL credentials:")
print("(If you don't know these, check MySQL Workbench or your installation notes)")
print()

host = input("MySQL Host (default: localhost): ").strip() or "localhost"
port = input("MySQL Port (default: 3306): ").strip() or "3306"
user = input("MySQL Username (default: root): ").strip() or "root"
password = input("MySQL Password: ").strip()

print()
print("Attempting to connect...")

try:
    connection = pymysql.connect(
        host=host,
        port=int(port),
        user=user,
        password=password,
        charset='utf8mb4'
    )
    
    print("✅ SUCCESS! MySQL connection works!")
    print()
    
    # Check if database exists
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES LIKE 'id_card_tracker'")
    db_exists = cursor.fetchone()
    
    if db_exists:
        print("✅ Database 'id_card_tracker' already exists!")
    else:
        print("⚠️  Database 'id_card_tracker' does not exist yet.")
        print("   You'll need to create it (we can do this next).")
    
    connection.close()
    
    print()
    print("=" * 60)
    print("✅ MySQL is ready to use!")
    print("=" * 60)
    
except Exception as e:
    print()
    print("❌ Connection failed!")
    print(f"Error: {e}")
    print()
    print("Common issues:")
    print("1. Wrong password - check your MySQL root password")
    print("2. MySQL server not running - check Windows Services")
    print("3. Firewall blocking connection")
    print()
    print("You can also use MySQL Workbench to test the connection.")

