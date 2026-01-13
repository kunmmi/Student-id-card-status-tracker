#!/usr/bin/env python3
"""
Migration script to move data from SQLite to MySQL
Run this after setting up MySQL to copy existing data
"""

import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

def migrate_data():
    """Migrate data from SQLite to MySQL"""
    
    # Check if SQLite database exists
    sqlite_path = "instance/id_cards.db"
    if not os.path.exists(sqlite_path):
        print("❌ SQLite database not found. Nothing to migrate.")
        return
    
    print("=" * 60)
    print("Migrating Data from SQLite to MySQL")
    print("=" * 60)
    print()
    
    # Get MySQL credentials
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = int(os.getenv('DB_PORT', '3306'))
    db_user = os.getenv('DB_USER', 'tracker_user')
    db_password = os.getenv('DB_PASSWORD', '')
    db_name = os.getenv('DB_NAME', 'id_card_tracker')
    
    try:
        import pymysql
        
        # Connect to MySQL
        print("Connecting to MySQL...")
        mysql_conn = pymysql.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_name,
            charset='utf8mb4'
        )
        mysql_cursor = mysql_conn.cursor()
        print("✅ Connected to MySQL")
        
        # Connect to SQLite
        print("Connecting to SQLite...")
        sqlite_conn = sqlite3.connect(sqlite_path)
        sqlite_cursor = sqlite_conn.cursor()
        print("✅ Connected to SQLite")
        print()
        
        # Migrate Students
        print("Migrating students...")
        sqlite_cursor.execute("SELECT id, matric_number, name, department, status, date_created, date_updated FROM students")
        students = sqlite_cursor.fetchall()
        
        student_count = 0
        for student in students:
            try:
                mysql_cursor.execute("""
                    INSERT INTO students (id, matric_number, name, department, status, date_created, date_updated)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        name=VALUES(name),
                        department=VALUES(department),
                        status=VALUES(status),
                        date_updated=VALUES(date_updated)
                """, student)
                student_count += 1
            except Exception as e:
                print(f"⚠️  Error migrating student {student[1]}: {e}")
        
        print(f"✅ Migrated {student_count} students")
        
        # Migrate Admins
        print("Migrating admins...")
        sqlite_cursor.execute("SELECT id, username, password, email, full_name, date_created, last_login FROM admins")
        admins = sqlite_cursor.fetchall()
        
        admin_count = 0
        for admin in admins:
            try:
                mysql_cursor.execute("""
                    INSERT INTO admins (id, username, password, email, full_name, date_created, last_login)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        password=VALUES(password),
                        email=VALUES(email),
                        full_name=VALUES(full_name),
                        last_login=VALUES(last_login)
                """, admin)
                admin_count += 1
            except Exception as e:
                print(f"⚠️  Error migrating admin {admin[1]}: {e}")
        
        print(f"✅ Migrated {admin_count} admins")
        
        # Commit changes
        mysql_conn.commit()
        print()
        print("=" * 60)
        print("✅ Migration Complete!")
        print("=" * 60)
        print(f"Migrated {student_count} students and {admin_count} admins")
        print()
        print("You can now use MySQL as your database.")
        print("The SQLite database is still available as backup.")
        
        # Close connections
        mysql_conn.close()
        sqlite_conn.close()
        
    except ImportError:
        print("❌ PyMySQL not installed!")
        print("Install it with: pip install PyMySQL")
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    migrate_data()

