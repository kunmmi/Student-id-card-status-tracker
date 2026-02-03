# Deployment Guide - ID Card Tracker

This guide covers deploying the ID Card Tracker application to various platforms.

## Quick Deploy Options

### Option 1: Railway (Recommended - Easiest)

1. **Sign up at [Railway.app](https://railway.app)**

2. **Create New Project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Connect your GitHub account
   - Select `id_card_tracker` repository

3. **Configure Environment Variables:**
   - Go to Settings → Variables
   - Add:
     ```
     SECRET_KEY=your-secret-key-here-change-this
     FLASK_DEBUG=False
     PORT=5000
     ```

4. **Deploy:**
   - Railway will automatically detect Python
   - It will install dependencies from `requirements.txt`
   - The app will deploy automatically

5. **Access Your App:**
   - Railway provides a URL like: `https://your-app.railway.app`
   - Your app is live!

---

### Option 2: Render (Free Tier Available)

1. **Sign up at [Render.com](https://render.com)**

2. **Create New Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select `id_card_tracker`

3. **Configure:**
   - **Name:** id-card-tracker
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`

4. **Environment Variables:**
   - Add in Environment section:
     ```
     SECRET_KEY=your-secret-key-here
     FLASK_DEBUG=False
     ```

5. **Deploy:**
   - Click "Create Web Service"
   - Render will build and deploy your app
   - Get your URL: `https://id-card-tracker.onrender.com`

---

### Option 3: PythonAnywhere (Free Tier)

1. **Sign up at [PythonAnywhere.com](https://www.pythonanywhere.com)**

2. **Upload Your Code:**
   - Go to Files tab
   - Upload your project files
   - Or use Git: `git clone https://github.com/kunmmi/Student-id-card-status-tracker.git`

3. **Create Web App:**
   - Go to Web tab
   - Click "Add a new web app"
   - Select Flask
   - Choose Python 3.10

4. **Configure WSGI File:**
   - Edit the WSGI file:
   ```python
   import sys
   path = '/home/yourusername/Student-id-card-status-tracker'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app as application
   ```

5. **Set Environment Variables:**
   - In Web tab → Environment variables:
     ```
     SECRET_KEY=your-secret-key
     FLASK_DEBUG=False
     ```

6. **Reload:**
   - Click "Reload" button
   - Your app is live at: `https://yourusername.pythonanywhere.com`

---

### Option 4: Heroku (Paid - But Reliable)

1. **Install Heroku CLI:**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login:**
   ```bash
   heroku login
   ```

3. **Create App:**
   ```bash
   heroku create id-card-tracker
   ```

4. **Set Environment Variables:**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key-here
   heroku config:set FLASK_DEBUG=False
   ```

5. **Deploy:**
   ```bash
   git push heroku main
   ```

6. **Open App:**
   ```bash
   heroku open
   ```

---

## Pre-Deployment Checklist

- [ ] Update `SECRET_KEY` in environment variables
- [ ] Set `FLASK_DEBUG=False` for production
- [ ] Test locally with `gunicorn app:app`
- [ ] Ensure all dependencies are in `requirements.txt`
- [ ] Update default admin password
- [ ] Review security settings

---

## Environment Variables

Create a `.env` file (for local) or set in your platform:

```env
SECRET_KEY=your-very-secret-key-change-this-in-production
FLASK_DEBUG=False
PORT=5000
DB_TYPE=sqlite
```

For production with MySQL:
```env
SECRET_KEY=your-secret-key
FLASK_DEBUG=False
DB_TYPE=mysql
DB_HOST=your-db-host
DB_PORT=3306
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_NAME=id_card_tracker
```

---

## Testing Locally Before Deploy

1. **Install gunicorn:**
   ```bash
   pip install gunicorn
   ```

2. **Test production server:**
   ```bash
   gunicorn app:app
   ```

3. **Access at:** `http://localhost:8000`

---

## Database Considerations

### SQLite (Default - Good for small apps)
- Works out of the box
- No setup needed
- File-based database
- **Note:** On some platforms (like Heroku), SQLite files are ephemeral and will be lost on restart

### MySQL/PostgreSQL (Recommended for Production)
- More reliable for production
- Persistent data storage
- Better for multiple users
- Requires database setup on your platform

---

## Troubleshooting

### App won't start:
- Check logs on your platform
- Verify `Procfile` exists
- Ensure `requirements.txt` is correct
- Check environment variables are set

### Database errors:
- Verify database connection settings
- Check if database tables are created
- Run migrations if needed

### Static files not loading:
- Check `static/` folder is included
- Verify file paths in templates

---

## Post-Deployment

1. **Change default admin password:**
   - Login with default credentials
   - Update password immediately

2. **Test all features:**
   - Student search
   - Admin login
   - File upload
   - Status updates

3. **Monitor logs:**
   - Check for errors
   - Monitor performance

---

## Support

For deployment issues, check:
- Platform-specific documentation
- Application logs
- GitHub Issues

---

**Good luck with your deployment!** 🚀

