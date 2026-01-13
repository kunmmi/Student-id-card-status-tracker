# MySQL Setup Guide for ID Card Tracker

## Step 1: Install MySQL Server

1. Download MySQL Community Server from: https://dev.mysql.com/downloads/mysql/
2. Choose: **Windows (x86, 64-bit), MSI Installer**
3. During installation:
   - Choose "Developer Default" or "Server only"
   - Set a **root password** (remember this!)
   - Keep default port: **3306**
   - Start MySQL as a Windows Service

## Step 2: Verify MySQL is Running

1. Open Command Prompt or PowerShell
2. Run: `mysql --version`
   - If you see a version number, MySQL is installed
   - If not, add MySQL to your PATH or use MySQL Workbench

## Step 3: Create Database and User

### Option A: Using MySQL Workbench (Easier)
1. Open MySQL Workbench
2. Connect to your MySQL server (use root password)
3. Run these SQL commands:

```sql
-- Create database
CREATE DATABASE id_card_tracker CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create user (replace 'your_password' with a strong password)
CREATE USER 'tracker_user'@'localhost' IDENTIFIED BY 'your_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON id_card_tracker.* TO 'tracker_user'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;
```

### Option B: Using Command Line
1. Open Command Prompt
2. Run: `mysql -u root -p`
3. Enter your root password
4. Run the SQL commands above

## Step 4: Test Connection

Run this Python script to test:

```python
import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='tracker_user',
        password='your_password',
        database='id_card_tracker'
    )
    print("✅ MySQL connection successful!")
    connection.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")
```

## Step 5: Update Application

The code will be updated to use MySQL. You'll need to:
1. Install PyMySQL: `pip install PyMySQL`
2. Update database connection string
3. Run the app - tables will be created automatically

## Step 6: Migrate Existing Data (if any)

If you have data in SQLite, we'll create a migration script to copy it to MySQL.

