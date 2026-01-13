#!/usr/bin/env python3
"""
Migration script to convert matric numbers from YYYY/XXXXXX format to XXXXXX format.
Run this script after updating the application to convert existing data.
"""

import sqlite3
import os
import shutil
from pathlib import Path
from datetime import datetime

def migrate_matric_numbers():
    """Convert existing matric numbers from YYYY/XXXXXX to XXXXXX format"""
    
    # Get the script directory and find the database
    script_dir = Path(__file__).parent
    db_path = script_dir / "instance" / "id_cards.db"
    
    # Also check parent directory (in case script is in id_card_tracker subfolder)
    if not db_path.exists():
        db_path = script_dir.parent / "instance" / "id_cards.db"
    
    if not db_path.exists():
        print("Database not found. Make sure the application has been run at least once.")
        return
    
    # Create a backup of the database before migration
    backup_path = db_path.with_suffix(f'.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.db')
    print(f"Creating database backup: {backup_path}")
    shutil.copy2(db_path, backup_path)
    print("Backup created successfully!")
    
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Get all existing matric numbers
        cursor.execute("SELECT id, matric_number FROM students")
        students = cursor.fetchall()
        
        if not students:
            print("No students found in the database.")
            return
        
        print(f"Found {len(students)} students to migrate...")
        
        # Process each student
        updated_count = 0
        for student_id, old_matric in students:
            # Check if the matric number is in the old format
            if '/' in old_matric:
                # Extract the 6-digit part after the slash
                parts = old_matric.split('/')
                if len(parts) == 2 and len(parts[1]) == 6:
                    new_matric = parts[1]
                    
                    # Update the database
                    cursor.execute(
                        "UPDATE students SET matric_number = ? WHERE id = ?",
                        (new_matric, student_id)
                    )
                    
                    print(f"Updated student {student_id}: {old_matric} -> {new_matric}")
                    updated_count += 1
                else:
                    print(f"Warning: Could not parse matric number '{old_matric}' for student {student_id}")
            else:
                print(f"Student {student_id} already has correct format: {old_matric}")
        
        # Commit the changes
        conn.commit()
        print(f"\nMigration completed! Updated {updated_count} students.")
        
    except Exception as e:
        print(f"Error during migration: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    print("Starting matric number migration...")
    print("This will convert matric numbers from YYYY/XXXXXX to XXXXXX format.")
    
    response = input("Do you want to continue? (y/N): ")
    if response.lower() in ['y', 'yes']:
        migrate_matric_numbers()
    else:
        print("Migration cancelled.")
