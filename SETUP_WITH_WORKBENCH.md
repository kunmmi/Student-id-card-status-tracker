# Setting Up MySQL with Workbench - Step by Step

## Step 1: Open MySQL Workbench

1. Open **MySQL Workbench** from your Start Menu
2. You should see a connection (usually called "Local instance MySQL95" or similar)
3. **Double-click** on it to connect
4. Enter your **root password** when prompted
5. Click **OK**

## Step 2: Create the Database

Once connected, you'll see a SQL editor window. Follow these steps:

1. **Click on the SQL editor tab** (or open a new query tab)
2. **Copy and paste** this SQL code:

```sql
-- Create the database
CREATE DATABASE id_card_tracker CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create a user for the application
CREATE USER 'tracker_user'@'localhost' IDENTIFIED BY 'tracker_password_123';

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON id_card_tracker.* TO 'tracker_user'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
```

3. **Click the lightning bolt icon** (⚡) or press `Ctrl+Enter` to execute
4. You should see "Success" messages for each command

**Important:** 
- Replace `'tracker_password_123'` with a strong password of your choice
- **Remember this password** - you'll need it for the `.env` file!

## Step 3: Verify Database Was Created

1. In the left sidebar, click the **refresh icon** (🔄) next to "SCHEMAS"
2. You should now see **`id_card_tracker`** in the list of databases
3. If you see it, you're good to go! ✅

## Step 4: Test Connection from Python

Now let's test if everything works:

1. Run: `python setup_mysql.py`
2. When prompted, enter:
   - Host: `localhost` (or just press Enter)
   - Port: `3306` (or just press Enter)
   - Username: `tracker_user`
   - Password: `tracker_password_123` (or whatever you set)
   - Database: `id_card_tracker` (or just press Enter)

3. If successful, it will create a `.env` file automatically!

## Step 5: Run Your Application

Once the `.env` file is created:

```bash
python app.py
```

The app will:
- Connect to MySQL
- Create all tables automatically
- Create default admin user

## Troubleshooting

**Can't connect to MySQL?**
- Make sure MySQL service is running (we confirmed it is)
- Check your root password is correct
- Try restarting MySQL service

**Permission denied?**
- Make sure you ran the GRANT command
- Make sure you ran FLUSH PRIVILEGES

**Database already exists?**
- That's fine! The app will use the existing database
- Or you can drop it and recreate: `DROP DATABASE id_card_tracker;`

