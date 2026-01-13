# University of Ibadan ID Card Collection Status Tracker

A web application for tracking the status of student ID cards at the University of Ibadan. Students can check their ID card status using their matriculation number, while ITEMS staff can manage student records and update statuses.

## Features

### For Students
- **Status Check**: Enter matric number to view ID card status
- **Mobile-Friendly**: Responsive design that works on all devices
- **Real-time Updates**: See current status and last update time

### For ITEMS Staff (Admin)
- **Secure Login**: Protected admin panel for staff access
- **Student Management**: View, search, and filter all student records
- **Status Updates**: Change student status via dropdown menus
- **Bulk Upload**: Upload Excel/CSV files to update multiple students
- **Dashboard**: Overview of statistics and student counts

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite (easily upgradeable to PostgreSQL/MySQL)
- **Frontend**: Bootstrap 5 + Bootstrap Icons
- **Authentication**: Flask-Login
- **File Processing**: Pandas + OpenPyXL
- **Responsive Design**: Mobile-first approach

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone/Download the Project
```bash
# If using git
git clone <repository-url>
cd id_card_tracker

# Or download and extract the ZIP file
cd id_card_tracker
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000`

## Default Admin Credentials

**Username**: `admin`  
**Password**: `admin123`

⚠️ **Important**: Change these credentials in production!

## Database Schema

### Students Table
- `id`: Primary key
- `matric_number`: Unique matriculation number (e.g., "2021/123456")
- `name`: Full student name
- `department`: Student's department
- `status`: ID card status (Not Yet Printed, Printing in Progress, Ready for Pickup, Collected)
- `date_created`: Record creation timestamp
- `date_updated`: Last update timestamp

### Admins Table
- `id`: Primary key
- `username`: Admin username
- `password`: Hashed password
- `email`: Admin email (optional)
- `full_name`: Admin's full name (optional)
- `date_created`: Account creation timestamp
- `last_login`: Last login timestamp

## File Upload Format

### Required Columns
Your Excel/CSV file must contain these columns:

| Column | Description | Example |
|--------|-------------|---------|
| `matric_number` | Student matriculation number | 2021/123456 |
| `name` | Full student name | John Doe |
| `department` | Student's department | Computer Science |
| `status` | ID card status | Not Yet Printed |

### Supported Status Values
- `Not Yet Printed`
- `Printing in Progress`
- `Ready for Pickup`
- `Collected`

### File Formats
- CSV (.csv)
- Excel (.xlsx, .xls)

## Usage Guide

### For Students
1. Visit the homepage
2. Click "Check My Status"
3. Enter your matriculation number
4. View your ID card status and information

### For ITEMS Staff
1. Click "Staff Login" on the homepage
2. Enter admin credentials
3. Use the dashboard to:
   - View all student records
   - Search and filter students
   - Update individual student statuses
   - Upload bulk data files

## API Endpoints

### Public Routes
- `GET /` - Homepage
- `GET /search` - Student search form
- `POST /search` - Process student search

### Admin Routes (Protected)
- `GET /admin/login` - Admin login form
- `POST /admin/login` - Process admin login
- `GET /admin/dashboard` - Admin dashboard
- `GET /admin/upload` - File upload form
- `POST /admin/upload` - Process file upload
- `POST /admin/update_status` - Update student status (AJAX)
- `GET /admin/logout` - Admin logout

## Customization

### Changing Status Values
Edit the status options in:
- `templates/admin_dashboard.html` (dropdown options)
- `templates/search.html` (status legend)
- `templates/index.html` (status types section)

### Adding New Fields
1. Update the database models in `models/database.py`
2. Modify the upload processing in `app.py`
3. Update templates to display new fields

### Changing Data Source
The application is designed to easily swap data sources:

1. **Current**: Excel/CSV file uploads
2. **Future**: MIS API integration
3. **Custom**: Modify the `admin_upload` route in `app.py`

## Security Considerations

### Production Deployment
- Change the default admin credentials
- Use environment variables for sensitive data
- Set `SECRET_KEY` to a strong random string
- Enable HTTPS
- Consider using a production WSGI server (Gunicorn, uWSGI)
- Use a production database (PostgreSQL, MySQL)

### File Upload Security
- File type validation
- File size limits
- Input sanitization
- Error handling

## Troubleshooting

### Common Issues

**Database errors**: Ensure the `models` folder contains `__init__.py` and `database.py`

**Import errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`

**File upload fails**: Check file format and ensure required columns are present

**Admin login fails**: Verify the database was created and default admin user exists

### Logs
Check the console output for error messages and debugging information.

## Future Enhancements

- **MIS Integration**: Pull student data directly from University MIS
- **Email Notifications**: Alert students when their ID card is ready
- **QR Code Generation**: Generate QR codes for easy collection verification
- **Advanced Reporting**: Export reports and analytics
- **Multi-language Support**: Support for multiple languages
- **API Access**: RESTful API for external integrations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is developed for the University of Ibadan. Please contact the ITEMS department for usage permissions.

## Support

For technical support or questions about the application, please contact the ITEMS department at the University of Ibadan.

---

**Developed for University of Ibadan ITEMS Department**  
**Version**: 1.0.0  
**Last Updated**: August 2024 