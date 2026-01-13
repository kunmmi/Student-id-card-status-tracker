# Documentation Generation Prompt for GPT-5

Copy and paste the following prompt to GPT-5 or any advanced AI assistant to generate comprehensive documentation for this project:

---

## PROMPT START

I need you to generate comprehensive, professional documentation for my final year project in Computer Science at the University of Ibadan. This is an ID Card Collection Status Tracker system.

### PROJECT OVERVIEW

**Project Title**: University of Ibadan ID Card Collection Status Tracker

**Project Type**: Final Year Project (Computer Science)

**Institution**: University of Ibadan

**Purpose**: A web-based application that allows students to check their ID card collection status using their matriculation number, while ITEMS (Information Technology and Media Services) staff can manage student records, update statuses, and perform bulk uploads.

### TECHNICAL STACK

- **Backend Framework**: Flask (Python 3.8+)
- **Database**: SQLite (default, with MySQL support)
- **ORM**: Flask-SQLAlchemy
- **Authentication**: Flask-Login
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Data Processing**: Pandas, OpenPyXL
- **Additional**: Python-dotenv for environment variables, PyMySQL for MySQL support

### KEY FEATURES

1. **Student Portal**:
   - Search ID card status by matriculation number
   - View current status and last update time
   - Mobile-responsive design

2. **Admin Dashboard** (ITEMS Staff):
   - Secure login system
   - View all student records
   - Search and filter functionality
   - Update individual student statuses via dropdown
   - Bulk upload via Excel/CSV files
   - Dashboard statistics

3. **Status Management**:
   - Not Yet Printed
   - Printing in Progress
   - Ready for Pickup
   - Collected

4. **Desktop Application**:
   - Standalone desktop app version
   - Launches web server and opens browser
   - Tkinter-based wrapper

### PROJECT STRUCTURE

```
id_card_tracker/
├── app.py                          # Main Flask application
├── desktop_app.py                  # Desktop application wrapper
├── lasu_desktop_app.py            # Alternative desktop app (Tkinter)
├── models/
│   ├── __init__.py
│   └── database.py                # Database models (Student, Admin)
├── templates/                      # HTML templates
│   ├── base.html
│   ├── index.html                 # Homepage
│   ├── search.html                # Student search form
│   ├── search_result.html         # Search results
│   ├── admin_login.html           # Admin login page
│   ├── admin_dashboard.html       # Admin dashboard
│   └── admin_upload.html          # Bulk upload page
├── static/
│   ├── css/                       # Stylesheets
│   └── js/                        # JavaScript files
├── instance/
│   └── id_cards.db                # SQLite database
├── requirements.txt               # Python dependencies
├── README.md                      # Basic project documentation
├── setup_mysql.py                 # MySQL setup script
├── migrate_to_mysql.py            # Database migration script
└── sample_students.csv           # Sample data file
```

### DATABASE SCHEMA

**Students Table**:
- id (Primary Key)
- matric_number (String, Unique, Indexed, 6 digits)
- name (String)
- department (String)
- status (String: Not Yet Printed, Printing in Progress, Ready for Pickup, Collected)
- date_created (DateTime)
- date_updated (DateTime)

**Admins Table**:
- id (Primary Key)
- username (String, Unique)
- password (String, Hashed)
- email (String, Optional)
- full_name (String, Optional)
- date_created (DateTime)
- last_login (DateTime)

### API ROUTES

**Public Routes**:
- GET `/` - Homepage
- GET `/search` - Student search form
- POST `/search` - Process student search

**Admin Routes** (Protected):
- GET `/admin/login` - Admin login form
- POST `/admin/login` - Process admin login
- GET `/admin/dashboard` - Admin dashboard
- GET `/admin/upload` - File upload form
- POST `/admin/upload` - Process bulk file upload
- POST `/admin/update_status` - Update student status (AJAX)
- GET `/admin/logout` - Admin logout

### SECURITY FEATURES

- Password hashing using Werkzeug
- Session management with Flask-Login
- Protected admin routes
- File upload validation
- Input sanitization for matric numbers

### DEPENDENCIES

```
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-Login==0.6.3
Flask-WTF==1.1.1
WTForms==3.0.1
numpy==1.26.4
pandas==2.1.1
openpyxl==3.1.2
Werkzeug==2.3.7
python-dotenv==1.0.0
PyMySQL==1.1.0
```

### DEFAULT CREDENTIALS

- Username: `admin`
- Password: `admin123`

### FILE UPLOAD FORMAT

CSV/Excel files must contain:
- matric_number (6 digits)
- name
- department
- status

### DOCUMENTATION REQUIREMENTS

Please generate comprehensive documentation that includes:

1. **Title Page**
   - Project title
   - Student name and details
   - University of Ibadan
   - Department of Computer Science
   - Academic year

2. **Abstract**
   - Brief overview (150-200 words)
   - Problem statement
   - Solution approach
   - Key achievements

3. **Table of Contents**

4. **Chapter 1: Introduction**
   - Background of the study
   - Problem statement
   - Objectives (General and Specific)
   - Significance of the study
   - Scope and limitations
   - Organization of the work

5. **Chapter 2: Literature Review**
   - Review of related works
   - Existing systems
   - Technology stack justification
   - Theoretical framework

6. **Chapter 3: System Analysis and Design**
   - System requirements (Functional and Non-functional)
   - System architecture
   - Database design (ERD, Schema)
   - Use case diagrams
   - System flowcharts
   - User interface design
   - Security considerations

7. **Chapter 4: Implementation**
   - Development environment
   - Technology choices and justification
   - Implementation details for each module:
     - Authentication module
     - Student search module
     - Admin dashboard module
     - File upload module
     - Database operations
   - Code snippets with explanations
   - Testing approach

8. **Chapter 5: Testing and Results**
   - Test cases
   - Test results
   - Screenshots of the application
   - Performance evaluation
   - User acceptance testing

9. **Chapter 6: Conclusion and Future Work**
   - Summary of achievements
   - Challenges encountered
   - Recommendations
   - Future enhancements:
     - MIS integration
     - Email notifications
     - QR code generation
     - Mobile app development
     - API development

10. **References**
    - Academic references
    - Technical documentation references
    - Framework documentation

11. **Appendices**
    - Complete source code listing (optional)
    - Database schema
    - Sample data
    - Installation guide
    - User manual

### DOCUMENTATION STYLE

- Use formal academic writing style
- Include diagrams where appropriate (describe them if you can't generate)
- Use proper citations
- Follow standard academic project documentation format
- Include code examples with proper formatting
- Add screenshots descriptions (mention where screenshots should be placed)
- Use clear section headings and subheadings
- Include page numbers
- Add table and figure captions

### ADDITIONAL CONTEXT

- This is a real-world application designed for the University of Ibadan ITEMS department
- The system handles sensitive student data
- It's designed to be scalable (can migrate from SQLite to MySQL/PostgreSQL)
- The application has both web and desktop versions
- Bulk upload feature supports CSV and Excel formats
- Matric numbers are validated to be exactly 6 digits
- The system is mobile-responsive

### SPECIAL INSTRUCTIONS

1. Make the documentation suitable for a final year project submission
2. Include proper academic citations
3. Explain technical decisions with justifications
4. Include UML diagrams descriptions (use case, class, sequence diagrams)
5. Provide detailed system architecture explanation
6. Include security considerations
7. Add performance analysis
8. Provide comprehensive testing documentation
9. Include user manual for both students and administrators
10. Add deployment guide

Please generate this documentation in a professional, academic format suitable for submission as a final year project in Computer Science.

## PROMPT END

---

### HOW TO USE THIS PROMPT

1. Copy the entire content between "## PROMPT START" and "## PROMPT END"
2. Paste it into GPT-5 or your preferred AI assistant
3. The AI will generate comprehensive documentation based on this prompt
4. Review and customize the generated documentation as needed
5. Add actual screenshots where mentioned
6. Include your personal details (name, matric number, etc.) in the title page

### TIPS FOR BETTER RESULTS

- You can ask the AI to generate specific sections if the full document is too long
- Request the AI to create diagrams in specific formats (Mermaid, PlantUML, etc.)
- Ask for code documentation in docstring format
- Request API documentation in OpenAPI/Swagger format
- Ask for database migration guides
- Request deployment guides for different platforms (Heroku, AWS, etc.)

---

**Note**: This prompt is designed to be comprehensive. You may want to break it into smaller sections if generating the entire document at once is too large for the AI model.

