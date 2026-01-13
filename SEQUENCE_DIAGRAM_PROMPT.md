# Sequence Diagram Prompts

Copy and paste these prompts to generate Sequence Diagrams for the ID Card Tracker system:

---

## PROMPT 1: STUDENT STATUS CHECK SEQUENCE DIAGRAM

**Copy this prompt for Student Status Check:**

```
Create a UML Sequence Diagram for the "Student Status Check" use case in the University of Ibadan ID Card Collection Status Tracker system.

ACTORS AND OBJECTS:
- Student (Actor)
- Web Browser (Boundary)
- FlaskApp (Controller)
- Search Process (Control)
- Student Model (Entity)
- Database (Entity)

SEQUENCE OF INTERACTIONS:

1. Student enters matric number in Web Browser
2. Student clicks "Check Status" button
3. Web Browser sends HTTP POST request to FlaskApp with matric number
4. FlaskApp receives request and calls Search Process
5. Search Process validates matric number (must be 6 digits)
6. Search Process queries Student Model
7. Student Model sends SQL query to Database
8. Database returns student record (or null if not found)
9. Student Model returns Student object to Search Process
10. Search Process checks if student exists
11a. If student found: Search Process returns student data to FlaskApp
11b. If student not found: Search Process returns error message to FlaskApp
12. FlaskApp renders search_result.html template with student data (or error message)
13. FlaskApp sends HTTP response to Web Browser
14. Web Browser displays status information to Student

ALTERNATIVE FLOW (Error Cases):
- If matric number invalid: Show validation error
- If student not found: Show "Student not found" message

DIAGRAM SPECIFICATIONS:
- Use standard UML Sequence Diagram notation
- Show lifelines for all actors and objects
- Show activation boxes on lifelines
- Use arrows for messages (solid for synchronous, dashed for return)
- Label all messages clearly
- Show alternative flows with alt/opt frames
- Include timing constraints if relevant
- Professional appearance suitable for academic documentation

Generate a complete Sequence Diagram for Student Status Check scenario.
```

---

## PROMPT 2: ADMIN LOGIN SEQUENCE DIAGRAM

**Copy this prompt for Admin Login:**

```
Create a UML Sequence Diagram for the "Admin Login" use case in the University of Ibadan ID Card Collection Status Tracker system.

ACTORS AND OBJECTS:
- ITEMS Staff (Actor)
- Web Browser (Boundary)
- FlaskApp (Controller)
- Authentication Process (Control)
- Admin Model (Entity)
- Database (Entity)
- LoginManager (Security)
- Session Storage (Entity)

SEQUENCE OF INTERACTIONS:

1. ITEMS Staff navigates to admin login page
2. Web Browser sends HTTP GET request to FlaskApp (/admin/login)
3. FlaskApp renders admin_login.html template
4. FlaskApp sends login form to Web Browser
5. Web Browser displays login form to ITEMS Staff
6. ITEMS Staff enters username and password
7. ITEMS Staff clicks "Login" button
8. Web Browser sends HTTP POST request to FlaskApp with credentials
9. FlaskApp receives credentials and calls Authentication Process
10. Authentication Process queries Admin Model with username
11. Admin Model sends SQL query to Database
12. Database returns Admin record (or null if not found)
13. Admin Model returns Admin object to Authentication Process
14. Authentication Process calls Admin.check_password(password)
15. Admin Model hashes provided password and compares with stored hash
16. Admin Model returns authentication result (true/false) to Authentication Process
17a. If authentication successful:
    17a1. Authentication Process calls LoginManager.login_user(admin)
    17a2. LoginManager creates session token
    17a3. LoginManager stores session in Session Storage
    17a4. LoginManager returns success to Authentication Process
    17a5. Authentication Process redirects to admin dashboard
17b. If authentication failed:
    17b1. Authentication Process returns error message
    17b2. FlaskApp renders login page with error message
18. FlaskApp sends HTTP response to Web Browser
19. Web Browser displays dashboard (success) or login page with error (failure)

DIAGRAM SPECIFICATIONS:
- Use standard UML Sequence Diagram notation
- Show lifelines for all actors and objects
- Show activation boxes on lifelines
- Use arrows for messages (solid for synchronous, dashed for return)
- Use alt frame for success/failure scenarios
- Label all messages clearly
- Show password hashing process
- Show session creation
- Professional appearance suitable for academic documentation

Generate a complete Sequence Diagram for Admin Login scenario.
```

---

## PROMPT 3: ADMIN STATUS UPDATE SEQUENCE DIAGRAM

**Copy this prompt for Admin Status Update:**

```
Create a UML Sequence Diagram for the "Admin Update Student Status" use case in the University of Ibadan ID Card Collection Status Tracker system.

ACTORS AND OBJECTS:
- ITEMS Staff (Actor)
- Web Browser (Boundary)
- FlaskApp (Controller)
- Status Update Process (Control)
- Student Model (Entity)
- Database (Entity)
- LoginManager (Security)

SEQUENCE OF INTERACTIONS:

1. ITEMS Staff is already logged in (session active)
2. ITEMS Staff views student record in dashboard
3. ITEMS Staff selects new status from dropdown menu
4. ITEMS Staff clicks "Update" button
5. Web Browser sends AJAX POST request to FlaskApp (/admin/update_status) with JSON data (student_id, new_status)
6. FlaskApp receives request
7. FlaskApp checks authentication via LoginManager.login_required decorator
8. LoginManager validates session token
9. LoginManager returns authentication status to FlaskApp
10. FlaskApp calls Status Update Process
11. Status Update Process queries Student Model with student_id
12. Student Model sends SQL query to Database
13. Database returns Student record
14. Student Model returns Student object to Status Update Process
15. Status Update Process validates new status value
16. Status Update Process updates Student.status = new_status
17. Status Update Process updates Student.date_updated = current_time
18. Status Update Process calls Student Model to save changes
19. Student Model sends UPDATE SQL query to Database
20. Database commits transaction
21. Database returns success confirmation to Student Model
22. Student Model returns success to Status Update Process
23. Status Update Process returns JSON response {success: true, message: "Status updated"} to FlaskApp
24. FlaskApp sends HTTP JSON response to Web Browser
25. Web Browser receives response and updates UI (shows success message, updates status display)
26. Web Browser displays updated status to ITEMS Staff

ERROR HANDLING:
- If student not found: Return JSON {success: false, message: "Student not found"}
- If authentication fails: Return 401 Unauthorized
- If database error: Rollback transaction and return error

DIAGRAM SPECIFICATIONS:
- Use standard UML Sequence Diagram notation
- Show lifelines for all actors and objects
- Show activation boxes on lifelines
- Use arrows for messages (solid for synchronous, dashed for return)
- Show AJAX request/response
- Show authentication check
- Show database transaction (commit)
- Use opt/alt frames for error handling
- Label all messages clearly
- Professional appearance suitable for academic documentation

Generate a complete Sequence Diagram for Admin Status Update scenario.
```

---

## PROMPT 4: BULK FILE UPLOAD SEQUENCE DIAGRAM

**Copy this prompt for Bulk File Upload:**

```
Create a UML Sequence Diagram for the "Admin Bulk File Upload" use case in the University of Ibadan ID Card Collection Status Tracker system.

ACTORS AND OBJECTS:
- ITEMS Staff (Actor)
- Web Browser (Boundary)
- FlaskApp (Controller)
- File Upload Process (Control)
- File Validation Process (Control)
- Pandas Library (Utility)
- Student Model (Entity)
- Database (Entity)
- LoginManager (Security)

SEQUENCE OF INTERACTIONS:

1. ITEMS Staff is already logged in (session active)
2. ITEMS Staff navigates to upload page
3. Web Browser sends HTTP GET request to FlaskApp (/admin/upload)
4. FlaskApp checks authentication via LoginManager
5. FlaskApp renders admin_upload.html template
6. FlaskApp sends upload form to Web Browser
7. Web Browser displays upload form to ITEMS Staff
8. ITEMS Staff selects CSV/Excel file
9. ITEMS Staff clicks "Upload" button
10. Web Browser sends HTTP POST request with multipart/form-data (file) to FlaskApp
11. FlaskApp receives request and checks authentication
12. FlaskApp validates file type (CSV, XLSX, XLS)
13. FlaskApp calls File Upload Process
14. File Upload Process calls Pandas Library to read file
15a. If CSV file: Pandas reads CSV using pd.read_csv()
15b. If Excel file: Pandas reads Excel using pd.read_excel()
16. Pandas Library returns DataFrame to File Upload Process
17. File Upload Process iterates through each row in DataFrame
18. For each row:
    18a. File Upload Process calls File Validation Process
    18b. File Validation Process validates matric_number (must be 6 digits)
    18c. File Validation Process validates required fields (name, department, status)
    18d. File Validation Process returns validation result
    18e. If valid:
        18e1. File Upload Process queries Student Model with matric_number
        18e2. Student Model queries Database
        18e3. Database returns Student record (or null)
        18e4. If student exists:
            18e4a. File Upload Process updates existing Student record
        18e5. If student does not exist:
            18e5a. File Upload Process creates new Student record
        18e6. File Upload Process adds/updates Student in batch
    18f. If invalid: Skip row and continue
19. File Upload Process commits all changes to Database
20. Database executes batch INSERT/UPDATE queries
21. Database commits transaction
22. Database returns success confirmation
23. File Upload Process counts successful records
24. File Upload Process returns success message with count to FlaskApp
25. FlaskApp flashes success message
26. FlaskApp redirects to admin dashboard
27. FlaskApp sends HTTP redirect response to Web Browser
28. Web Browser displays dashboard with success message to ITEMS Staff

ERROR HANDLING:
- If file type invalid: Return error message
- If file processing fails: Rollback transaction, return error
- If validation fails for rows: Skip invalid rows, process valid ones

DIAGRAM SPECIFICATIONS:
- Use standard UML Sequence Diagram notation
- Show lifelines for all actors and objects
- Show activation boxes on lifelines
- Use arrows for messages (solid for synchronous, dashed for return)
- Show loop frame for row iteration
- Show file reading process
- Show validation process
- Show batch database operations
- Use opt/alt frames for error handling
- Label all messages clearly
- Professional appearance suitable for academic documentation

Generate a complete Sequence Diagram for Bulk File Upload scenario.
```

---

## PROMPT 5: COMPLETE SYSTEM SEQUENCE DIAGRAM

**Copy this prompt for Overview Sequence Diagram:**

```
Create a comprehensive UML Sequence Diagram showing the overall interaction flow in the University of Ibadan ID Card Collection Status Tracker system.

ACTORS AND OBJECTS:
- Student (Actor)
- ITEMS Staff (Actor)
- Web Browser (Boundary)
- FlaskApp (Controller)
- Database (Entity)
- LoginManager (Security)

SHOW THREE MAIN SCENARIOS:

SCENARIO 1: Student Status Check
1. Student → Web Browser: Enter matric number
2. Web Browser → FlaskApp: POST /search (matric_number)
3. FlaskApp → Database: Query student by matric_number
4. Database → FlaskApp: Return student record
5. FlaskApp → Web Browser: Render search_result.html
6. Web Browser → Student: Display status

SCENARIO 2: Admin Login and Dashboard Access
1. ITEMS Staff → Web Browser: Navigate to /admin/login
2. Web Browser → FlaskApp: GET /admin/login
3. FlaskApp → Web Browser: Render login form
4. ITEMS Staff → Web Browser: Submit credentials
5. Web Browser → FlaskApp: POST /admin/login (username, password)
6. FlaskApp → LoginManager: Authenticate user
7. LoginManager → Database: Query admin by username
8. Database → LoginManager: Return admin record
9. LoginManager → FlaskApp: Authentication success
10. FlaskApp → Web Browser: Redirect to /admin/dashboard
11. Web Browser → FlaskApp: GET /admin/dashboard
12. FlaskApp → Database: Query all students
13. Database → FlaskApp: Return student records
14. FlaskApp → Web Browser: Render admin_dashboard.html
15. Web Browser → ITEMS Staff: Display dashboard

SCENARIO 3: Admin Status Update
1. ITEMS Staff → Web Browser: Select new status
2. Web Browser → FlaskApp: POST /admin/update_status (JSON)
3. FlaskApp → LoginManager: Verify session
4. FlaskApp → Database: UPDATE student status
5. Database → FlaskApp: Confirmation
6. FlaskApp → Web Browser: JSON response
7. Web Browser → ITEMS Staff: Updated status displayed

DIAGRAM SPECIFICATIONS:
- Use standard UML Sequence Diagram notation
- Show all actors and objects as lifelines
- Use separate frames (sd) for each scenario or show as parallel flows
- Show activation boxes
- Label all messages clearly
- Show return messages (dashed arrows)
- Professional appearance suitable for academic documentation

Generate a comprehensive Sequence Diagram showing all main system interactions.
```

---

## HOW TO USE

### In Miro AI:
1. Open Miro board
2. Click AI icon or press `/` and type "AI"
3. Select "Generate diagram" or "Create with AI"
4. Copy and paste ONE of the prompts above
5. Click Generate
6. Customize as needed

### In Other Tools:
- **Draw.io**: Use prompt to get description, then create manually
- **Lucidchart**: Use AI feature with the prompt
- **PlantUML**: Ask AI to convert to PlantUML code first
- **Visual Paradigm**: Use the prompt in their AI assistant

---

## QUICK REFERENCE: ALL SEQUENCE DIAGRAMS

**For your documentation, you may want to generate:**

1. ✅ **Student Status Check** - Most important for students
2. ✅ **Admin Login** - Shows authentication flow
3. ✅ **Admin Status Update** - Shows AJAX interaction
4. ✅ **Bulk File Upload** - Shows file processing
5. ✅ **Complete System Overview** - Shows all interactions

---

## TIPS FOR BEST RESULTS

1. **Generate One at a Time**: Use separate prompts for each scenario
2. **Be Specific**: Use the detailed prompts for better results
3. **Iterate**: Generate, review, and ask for refinements
4. **Add Details**: Request specific message parameters, return values
5. **Error Handling**: Ask to include error scenarios
6. **Timing**: Request timing constraints if needed

---

## FOLLOW-UP PROMPTS

After generating, refine with:

- "Add return messages (dashed arrows) for all method calls"
- "Show activation boxes on all lifelines"
- "Add timing constraints (e.g., < 1 second)"
- "Include error handling scenarios with alt frames"
- "Show loop frames for iteration processes"
- "Add notes explaining complex interactions"
- "Show synchronous vs asynchronous messages"

---

## READY-TO-USE: STUDENT STATUS CHECK (MOST IMPORTANT)

**Copy this for the most common use case:**

```
Create a UML Sequence Diagram for "Student Status Check" in the ID Card Tracker system.

Actors/Objects:
- Student
- Web Browser
- FlaskApp
- Student Model
- Database

Sequence:
1. Student enters matric number → Web Browser
2. Web Browser → FlaskApp: POST /search (matric_number)
3. FlaskApp → Student Model: query_by_matric(matric_number)
4. Student Model → Database: SELECT WHERE matric_number = ?
5. Database → Student Model: Student record
6. Student Model → FlaskApp: Student object
7. FlaskApp → Web Browser: Render search_result.html
8. Web Browser → Student: Display status

Use standard UML Sequence Diagram notation with lifelines, activation boxes, and labeled arrows.
```

---

**All prompts are ready to use! Copy the one you need and paste into your diagramming tool.**

