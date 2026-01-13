#!/usr/bin/env python3
"""
SQLite Database Viewer for ID Card Tracker
This script allows you to view the contents of the SQLite database
"""

import sqlite3
import os
from datetime import datetime

# Database path
db_path = os.path.join('instance', 'id_cards.db')

def print_table_structure(conn, table_name):
    """Print the structure of a table"""
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    
    print(f"\n{'='*80}")
    print(f"Table: {table_name}")
    print(f"{'='*80}")
    print(f"{'Column Name':<20} {'Type':<15} {'Not Null':<10} {'Default':<15} {'PK':<5}")
    print("-" * 80)
    for col in columns:
        cid, name, col_type, not_null, default_val, pk = col
        print(f"{name:<20} {col_type:<15} {'Yes' if not_null else 'No':<10} {str(default_val) if default_val else 'None':<15} {'Yes' if pk else 'No':<5}")
    print()

def print_table_data(conn, table_name):
    """Print all data from a table"""
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    # Get column names
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in cursor.fetchall()]
    
    if not rows:
        print(f"No data in {table_name} table.")
        return
    
    print(f"\n{'='*80}")
    print(f"Data in {table_name} table ({len(rows)} rows)")
    print(f"{'='*80}")
    
    # Print header
    header = " | ".join([f"{col:<15}" for col in columns])
    print(header)
    print("-" * len(header))
    
    # Print rows
    for row in rows:
        row_str = " | ".join([f"{str(val):<15}" if val is not None else f"{'None':<15}" for val in row])
        print(row_str)
    print()

def main():
    """Main function"""
    print("="*80)
    print("ID Card Tracker - SQLite Database Viewer")
    print("="*80)
    
    # Check if database exists
    if not os.path.exists(db_path):
        print(f"\n❌ Database file not found at: {db_path}")
        print("   The database will be created when you first run the Flask application.")
        print("   Please run 'python app.py' first to create the database.")
        return
    
    # Get file info
    file_size = os.path.getsize(db_path)
    file_time = datetime.fromtimestamp(os.path.getmtime(db_path))
    
    print(f"\n📁 Database Location: {os.path.abspath(db_path)}")
    print(f"📊 File Size: {file_size:,} bytes ({file_size/1024:.2f} KB)")
    print(f"🕒 Last Modified: {file_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [table[0] for table in cursor.fetchall()]
        
        if not tables:
            print("\n⚠️  No tables found in the database.")
            conn.close()
            return
        
        print(f"\n📋 Tables found: {', '.join(tables)}")
        
        # Show structure and data for each table
        for table in tables:
            print_table_structure(conn, table)
            print_table_data(conn, table)
        
        # Show statistics
        print("\n" + "="*80)
        print("Database Statistics")
        print("="*80)
        
        if 'students' in tables:
            cursor.execute("SELECT COUNT(*) FROM students")
            student_count = cursor.fetchone()[0]
            print(f"Total Students: {student_count}")
            
            cursor.execute("SELECT status, COUNT(*) FROM students GROUP BY status")
            status_counts = cursor.fetchall()
            print("\nStatus Distribution:")
            for status, count in status_counts:
                print(f"  {status}: {count}")
        
        if 'admins' in tables:
            cursor.execute("SELECT COUNT(*) FROM admins")
            admin_count = cursor.fetchone()[0]
            print(f"\nTotal Admins: {admin_count}")
        
        conn.close()
        print("\n✅ Database viewing complete!")
        
    except sqlite3.Error as e:
        print(f"\n❌ Database error: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == '__main__':
    main()

