# Railway Deployment Guide - Step by Step

## Quick Deploy to Railway

### Step 1: Sign Up / Login
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub (recommended) or email
3. Complete verification

### Step 2: Create New Project
1. Click **"New Project"** button
2. Select **"Deploy from GitHub repo"**
3. Authorize Railway to access your GitHub
4. Select repository: `Student-id-card-status-tracker`

### Step 3: Railway Auto-Detection
- Railway will automatically:
  - Detect Python
  - Install dependencies from `requirements.txt`
  - Use `Procfile` to start the app
  - Deploy your app

### Step 4: Set Environment Variables
1. Go to your project dashboard
2. Click on your service
3. Go to **"Variables"** tab
4. Click **"New Variable"**
5. Add these variables:

```
SECRET_KEY=your-secret-key-here-generate-a-strong-one
FLASK_DEBUG=False
PORT=5000
```

**To generate a secret key:**
```python
import secrets
print(secrets.token_hex(32))
```

Or use this online tool: https://randomkeygen.com/

### Step 5: Get Your App URL
1. Go to **"Settings"** tab
2. Under **"Domains"**, Railway provides a URL like:
   - `https://your-app-name.up.railway.app`
2. Click **"Generate Domain"** if needed
3. Your app is live!

### Step 6: Initialize Database
1. Visit your app URL
2. The app will automatically create the database on first run
3. Default admin credentials:
   - Username: `admin`
   - Password: `admin123`
4. **IMPORTANT:** Change the password immediately after first login!

---

## Troubleshooting

### App Won't Start
- Check **"Deployments"** tab for build logs
- Verify `Procfile` exists
- Ensure `requirements.txt` is correct
- Check environment variables are set

### Database Issues
- Railway uses SQLite by default (ephemeral - data may be lost on restart)
- For production, consider using Railway's PostgreSQL addon:
  1. Click **"New"** → **"Database"** → **"Add PostgreSQL"**
  2. Update environment variables:
     ```
     DB_TYPE=postgresql
     DATABASE_URL=${{Postgres.DATABASE_URL}}
     ```

### Static Files Not Loading
- Check file paths in templates
- Verify `static/` folder is included in repository

### Port Issues
- Railway automatically sets `PORT` environment variable
- Your app already uses `os.getenv('PORT', 5000)` - this is correct

---

## Post-Deployment Checklist

- [ ] App is accessible at Railway URL
- [ ] Homepage loads correctly
- [ ] Student search works
- [ ] Admin login works
- [ ] Dashboard displays
- [ ] File upload works
- [ ] Status updates work
- [ ] Changed default admin password

---

## Custom Domain (Optional)

1. Go to **"Settings"** → **"Domains"**
2. Click **"Custom Domain"**
3. Add your domain
4. Follow DNS configuration instructions

---

## Monitoring

- View logs: **"Deployments"** tab → Click on deployment → View logs
- Monitor usage: **"Metrics"** tab
- Check errors: **"Logs"** tab

---

## Updating Your App

1. Make changes to your code
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update app"
   git push
   ```
3. Railway will automatically redeploy!

---

## Support

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Check deployment logs for errors

---

**Your app should be live in minutes!** 🚀

