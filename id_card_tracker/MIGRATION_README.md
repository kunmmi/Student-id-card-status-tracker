# Matric Number Format Migration Guide

## Overview

The matric number format has been changed from `YYYY/XXXXXX` (4-digit year + slash + 6-digit number) to `XXXXXX` (6-digit number only).

## What Changed

-   **Before**: Matric numbers were in format `2021/123456`
-   **After**: Matric numbers are now in format `123456`

## Files Updated

The following files have been updated to reflect the new format:

1. **templates/search.html** - Updated form validation and JavaScript
2. **templates/admin_upload.html** - Updated sample data and documentation
3. **sample_students.csv** - Updated sample data
4. **README.md** - Updated documentation
5. **migrate_matric_numbers.py** - Migration script for existing data

## Migration Steps

### Step 1: Update the Application

The application code has already been updated to handle the new format.

### Step 2: Migrate Existing Data (if any)

If you have existing student data in the database with the old format, run the migration script:

```bash
python migrate_matric_numbers.py
```

This script will:

-   Connect to your existing database
-   Find all students with matric numbers in the old format
-   Convert them to the new format (removes the year and slash)
-   Update the database

### Step 3: Verify the Changes

After migration, verify that:

-   All matric numbers are now 6 digits
-   The search functionality works with the new format
-   Admin uploads work with the new format

## Important Notes

1. **Backup**: Always backup your database before running migrations
2. **Testing**: Test the application thoroughly after migration
3. **Data Integrity**: The migration script preserves the 6-digit portion of existing matric numbers
4. **New Entries**: All new student entries should use the 6-digit format

## Rollback (if needed)

If you need to rollback to the old format:

1. Restore your database backup
2. Revert the code changes
3. The old format will work again

## Support

If you encounter any issues during migration, check:

1. Database permissions
2. Python environment
3. Application logs
4. Database file integrity
