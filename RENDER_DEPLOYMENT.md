# Render Deployment Guide - Step by Step

## Quick Deploy to Render

### Step 1: Sign Up / Login
1. Go to [render.com](https://render.com)
2. Click **"Get Started for Free"**
3. Sign up with GitHub (recommended) or email
4. Complete email verification

### Step 2: Create New Web Service
1. Click **"New +"** button (top right)
2. Select **"Web Service"**
3. Connect your GitHub account (if not already connected)
4. Select repository: `Student-id-card-status-tracker`
5. Click **"Connect"**

### Step 3: Configure Your Service
Fill in the following settings:

**Basic Settings:**
- **Name:** `id-card-tracker` (or any name you prefer)
- **Region:** Choose closest to you (e.g., `Oregon (US West)`)
- **Branch:** `main`
- **Root Directory:** Leave empty (or `./` if needed)
- **Environment:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

**Advanced Settings (Optional):**
- **Auto-Deploy:** `Yes` (deploys on every push to main)

### Step 4: Set Environment Variables
Click **"Advanced"** → **"Add Environment Variable"** and add:

```
SECRET_KEY=30e61cd6dff44caa1f66291a3045348c4eee9c98c3598826a585f619b9216545
FLASK_DEBUG=False
```

**Or use Render's secret generator:**
- Click **"Generate"** next to SECRET_KEY field

### Step 5: Deploy
1. Scroll down and click **"Create Web Service"**
2. Render will start building your app
3. Watch the build logs in real-time
4. Build typically takes 2-5 minutes

### Step 6: Get Your App URL
1. Once deployment completes, Render provides a URL:
   - `https://id-card-tracker.onrender.com` (or your custom name)
2. Your app is live!

### Step 7: Initialize Database
1. Visit your Render URL
2. The app will automatically create the database on first run
3. Default admin credentials:
   - Username: `admin`
   - Password: `admin123`
4. **IMPORTANT:** Change the password immediately after first login!

---

## Render Free Tier Notes

**Important Limitations:**
- Services spin down after 15 minutes of inactivity
- First request after spin-down may take 30-60 seconds (cold start)
- Free tier includes:
  - 750 hours/month
  - 512 MB RAM
  - 0.5 CPU

**To prevent spin-down (optional):**
- Upgrade to paid plan, or
- Use a service like UptimeRobot to ping your app every 5 minutes

---

## Troubleshooting

### Build Fails
- Check build logs in Render dashboard
- Verify `requirements.txt` is correct
- Ensure Python version is compatible (3.8+)
- Check for any missing dependencies

### App Won't Start
- Check service logs in Render dashboard
- Verify `startCommand` is correct: `gunicorn app:app`
- Ensure `SECRET_KEY` environment variable is set
- Check port configuration (Render uses port 10000)

### Database Issues
- Render uses SQLite by default (ephemeral - data may be lost)
- For production, add PostgreSQL:
  1. Click **"New +"** → **"PostgreSQL"**
  2. Create database
  3. Get connection string from database dashboard
  4. Update environment variables:
     ```
     DB_TYPE=postgresql
     DATABASE_URL=<connection-string-from-render>
     ```

### Static Files Not Loading
- Check file paths in templates
- Verify `static/` folder is included in repository
- Check Render logs for 404 errors

### App Spins Down (Free Tier)
- First request after inactivity takes longer
- This is normal for free tier
- Consider upgrading or using uptime monitoring

---

## Post-Deployment Checklist

- [ ] App is accessible at Render URL
- [ ] Homepage loads correctly
- [ ] Student search works
- [ ] Admin login works
- [ ] Dashboard displays
- [ ] File upload works
- [ ] Status updates work
- [ ] Changed default admin password

---

## Custom Domain (Optional)

1. Go to your service dashboard
2. Click **"Settings"** tab
3. Scroll to **"Custom Domains"**
4. Click **"Add Custom Domain"**
5. Follow DNS configuration instructions

---

## Monitoring

- **View Logs:** Service dashboard → **"Logs"** tab
- **Metrics:** Service dashboard → **"Metrics"** tab
- **Events:** Service dashboard → **"Events"** tab

---

## Updating Your App

1. Make changes to your code
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update app"
   git push
   ```
3. Render will automatically redeploy (if auto-deploy is enabled)!

---

## Environment Variables Reference

```
SECRET_KEY=your-secret-key-here
FLASK_DEBUG=False
PORT=10000
DB_TYPE=sqlite
```

For PostgreSQL:
```
DB_TYPE=postgresql
DATABASE_URL=postgresql://user:pass@host:5432/dbname
```

---

## Support

- Render Docs: https://render.com/docs
- Render Status: https://status.render.com
- Check service logs for errors

---

## Quick Start Commands

**If using Render CLI:**
```bash
# Install Render CLI
npm install -g render-cli

# Login
render login

# Deploy
render deploy
```

---

**Your app should be live in 2-5 minutes!** 🚀

