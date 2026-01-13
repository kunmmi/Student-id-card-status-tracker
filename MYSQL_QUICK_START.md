# MySQL Quick Start Guide

## Complete Step-by-Step Process

### Step 1: Install MySQL Server
1. Download from: https://dev.mysql.com/downloads/mysql/
2. Install MySQL Community Server
3. Remember your **root password** during installation

### Step 2: Create Database and User

Open MySQL Workbench or Command Line and run:

```sql
CREATE DATABASE id_card_tracker CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'tracker_user'@'localhost' IDENTIFIED BY 'your_strong_password';

GRANT ALL PRIVILEGES ON id_card_tracker.* TO 'tracker_user'@'localhost';

FLUSH PRIVILEGES;
```

**Replace `your_strong_password` with your actual password!**

### Step 3: Install Python MySQL Driver

```bash
pip install PyMySQL
```

Or install all requirements:
```bash
pip install -r requirements.txt
```

### Step 4: Configure MySQL Connection

**Option A: Use Setup Script (Easiest)**
```bash
python setup_mysql.py
```
This will ask for your MySQL credentials and create a `.env` file automatically.

**Option B: Manual Configuration**
1. Create a `.env` file in the project root
2. Add these lines:
```
DB_TYPE=mysql
DB_HOST=localhost
DB_PORT=3306
DB_USER=tracker_user
DB_PASSWORD=your_strong_password
DB_NAME=id_card_tracker
SECRET_KEY=your-secret-key-change-this
```

### Step 5: Run the Application

```bash
python app.py
```

The app will:
- Connect to MySQL automatically
- Create all tables if they don't exist
- Create default admin user (username: `admin`, password: `admin123`)

### Step 6: Migrate Existing Data (Optional)

If you have data in SQLite and want to move it to MySQL:

```bash
python migrate_to_mysql.py
```

This will copy all students and admins from SQLite to MySQL.

## Switching Back to SQLite

To use SQLite again (for development), either:
- Delete the `.env` file, OR
- Set `DB_TYPE=sqlite` in `.env`

## Troubleshooting

**Connection Error?**
- Check MySQL server is running
- Verify credentials in `.env` file
- Test connection: `python setup_mysql.py`

**Tables not created?**
- Make sure database exists
- Check user has proper permissions
- Look for error messages in console

**Import Error?**
- Run: `pip install PyMySQL`
- Make sure it's in requirements.txt

## Security Notes

⚠️ **Important:**
- Never commit `.env` file to git (it's in .gitignore)
- Use strong passwords for MySQL
- Change default admin password after first login
- Use environment variables for production deployment

