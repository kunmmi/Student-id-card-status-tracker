# Admin Dashboard User Activity Diagram Prompt

Copy and paste this prompt to generate an Activity Diagram for the Admin Dashboard:

---

## PROMPT FOR MIRO AI / DIAGRAM TOOLS

Create a UML Activity Diagram showing the user activities and workflow in the Admin Dashboard of the University of Ibadan ID Card Collection Status Tracker system.

### Main Activities:

**Initial State:**
- Admin logs in successfully

**Main Activity Flow:**

1. **Access Dashboard**
   - Admin navigates to dashboard
   - System displays dashboard with statistics and student list

2. **View Statistics**
   - View total students count
   - View "Not Yet Printed" count
   - View "Printing in Progress" count
   - View "Ready for Pickup" count
   - View "Collected" count

3. **Search Students**
   - Enter search term (name or matric number)
   - System filters student list in real-time
   - Display filtered results

4. **Filter Students**
   - Filter by Status (dropdown)
   - Filter by Department (dropdown)
   - Apply multiple filters simultaneously
   - Clear filters

5. **Update Student Status**
   - Select student from table
   - Change status via dropdown menu
   - System sends AJAX request
   - System updates database
   - System displays success message
   - System refreshes statistics
   - System updates status badge color

6. **Upload Bulk Data**
   - Click "Upload Data" button
   - Navigate to upload page
   - Select CSV/Excel file
   - Upload file
   - System validates file
   - System processes file
   - System updates database
   - System redirects to dashboard
   - System displays success message

7. **Logout**
   - Click "Logout" button
   - System clears session
   - System redirects to homepage

### Decision Points:

- **After Search/Filter**: Are there results? (Yes → Display results, No → Show "No results" message)
- **After Status Update**: Was update successful? (Yes → Show success toast, No → Show error message)
- **After File Upload**: Was file valid? (Yes → Process, No → Show error)
- **After File Processing**: Were there errors? (Yes → Show error, No → Show success)

### Parallel Activities:

- Statistics update can happen in parallel with table display
- Search and filter can work simultaneously
- Multiple status updates can be processed independently

### Swimlanes (Optional):

- **Admin User**: User actions (click, select, enter)
- **Web Browser**: Client-side processing (filter, display)
- **Flask Application**: Server-side processing (query, update)
- **Database**: Data operations (select, update, insert)

### Diagram Specifications:

- Use standard UML Activity Diagram notation
- Show initial node (filled circle)
- Show activity nodes (rounded rectangles)
- Show decision nodes (diamonds)
- Show merge nodes (diamonds)
- Show fork/join nodes (horizontal bars) for parallel activities
- Show final nodes (filled circle with ring)
- Use control flows (arrows) between nodes
- Label all activities clearly
- Show guards on decision flows (e.g., [results found], [update successful])
- Use swimlanes to separate user, browser, application, and database activities
- Professional appearance suitable for academic documentation

Generate a comprehensive Activity Diagram for Admin Dashboard user activities.

---

## ALTERNATIVE: SIMPLIFIED PROMPT

**Quick Version:**

```
Create a UML Activity Diagram for Admin Dashboard activities in an ID Card Tracker system.

Activities:
- Access Dashboard
- View Statistics
- Search Students
- Filter by Status/Department
- Update Student Status
- Upload Bulk Data
- Logout

Show decision points for search results, update success, file validation.
Use standard UML Activity Diagram notation with initial/final nodes, activities, decisions, and flows.
```

---

## DETAILED PROMPT WITH ALL ACTIVITIES

**Complete Version for Best Results:**

```
Create a comprehensive UML Activity Diagram for the Admin Dashboard user activities in the University of Ibadan ID Card Collection Status Tracker system.

SWIMLANES:
1. Admin User (Actor)
2. Web Browser (Client)
3. Flask Application (Server)
4. Database (Data Layer)

INITIAL STATE:
- Admin successfully logged in

MAIN ACTIVITY FLOW:

[Initial Node] → Access Dashboard

ACTIVITY 1: Access Dashboard
- Admin navigates to /admin/dashboard
- Web Browser sends GET request
- Flask Application queries database for all students
- Database returns student records
- Flask Application calculates statistics
- Web Browser displays dashboard with:
  * Statistics cards (Total, Not Yet Printed, Printing, Ready, Collected)
  * Search and filter controls
  * Student records table

ACTIVITY 2: View Statistics
- System displays statistics cards:
  * Total Students count
  * Not Yet Printed count
  * Printing in Progress count
  * Ready for Pickup count
  * Collected count
- Statistics update automatically when data changes

ACTIVITY 3: Search Students
- Admin enters search term in search box
- Web Browser filters table rows in real-time
- [Decision: Results Found?]
  - [Yes] → Display filtered student rows
  - [No] → Display "No students found" message

ACTIVITY 4: Filter Students
- Admin selects status from dropdown
- Admin selects department from dropdown
- Web Browser applies filters simultaneously
- Web Browser filters table rows
- [Decision: Results Found?]
  - [Yes] → Display filtered rows
  - [No] → Display "No students found" message
- Admin can click "Clear" to reset filters

ACTIVITY 5: Update Student Status
- Admin selects status from dropdown in student row
- Web Browser sends AJAX POST request with student_id and new_status
- Flask Application receives request
- Flask Application queries database for student
- Database returns student record
- Flask Application updates student.status and student.date_updated
- Flask Application commits to database
- Database updates record
- [Decision: Update Successful?]
  - [Yes] → 
    * Flask Application returns JSON success
    * Web Browser updates status badge color
    * Web Browser displays success toast
    * Web Browser refreshes statistics (or reloads page)
  - [No] →
    * Flask Application returns JSON error
    * Web Browser displays error message
    * Web Browser resets dropdown to previous value

ACTIVITY 6: Upload Bulk Data
- Admin clicks "Upload Data" button
- Web Browser navigates to /admin/upload
- Flask Application renders upload form
- Admin selects CSV/Excel file
- Admin clicks "Upload" button
- Web Browser sends POST request with file
- Flask Application validates file type
- [Decision: File Valid?]
  - [Yes] →
    * Flask Application reads file (Pandas)
    * Flask Application validates each row
    * Flask Application processes rows:
      - For each row:
        * Check if student exists
        * If exists: Update record
        * If not exists: Create new record
    * Flask Application commits batch to database
    * Database inserts/updates records
    * [Decision: Processing Successful?]
      - [Yes] →
        * Flask Application redirects to dashboard
        * Web Browser displays success message
        * Dashboard refreshes with new data
      - [No] →
        * Flask Application rolls back transaction
        * Flask Application displays error message
  - [No] →
    * Flask Application displays file format error
    * Admin can select different file

ACTIVITY 7: Logout
- Admin clicks "Logout" button
- Web Browser sends GET request to /admin/logout
- Flask Application clears session
- Flask Application redirects to homepage
- Web Browser displays homepage

PARALLEL ACTIVITIES:
- Statistics calculation can run in parallel with table rendering
- Multiple status updates can be processed independently
- Search and filter operations run simultaneously

DECISION NODES:
1. [Results Found?] - After search/filter
2. [Update Successful?] - After status update
3. [File Valid?] - After file upload
4. [Processing Successful?] - After file processing

MERGE NODES:
- Merge after search/filter decision
- Merge after update decision
- Merge after file validation decision

FINAL STATES:
- Dashboard displayed
- Logout complete

DIAGRAM SPECIFICATIONS:
- Use standard UML Activity Diagram notation
- Initial node: Filled circle
- Activity nodes: Rounded rectangles with activity names
- Decision nodes: Diamonds with decision questions
- Merge nodes: Diamonds (same as decision but for merging flows)
- Fork/Join nodes: Horizontal bars for parallel activities
- Final nodes: Filled circle with ring
- Control flows: Arrows labeled with guards where appropriate
- Guards: [results found], [no results], [success], [error], [valid], [invalid]
- Swimlanes: Four lanes (Admin User, Web Browser, Flask Application, Database)
- Activity labels: Clear, descriptive names
- Professional layout suitable for academic documentation

Generate a comprehensive Activity Diagram showing all admin dashboard activities with proper swimlanes, decisions, and parallel activities.
```

---

## VISUAL LAYOUT DESCRIPTION

**For Better Understanding:**

```
[Initial] → Access Dashboard
              ↓
         View Statistics (parallel)
              ↓
         Display Student Table
              ↓
    ┌─────────────────────┐
    │  Search/Filter      │
    └──────────┬──────────┘
               ↓
    ┌─────────────────────┐
    │ [Results Found?]    │
    └───┬─────────────┬───┘
        │ Yes         │ No
        ↓             ↓
    Display Rows   Show Message
        │             │
        └─────┬───────┘
              ↓
    ┌─────────────────────┐
    │ Update Status?      │
    └──────────┬──────────┘
               ↓
         Send AJAX Request
               ↓
    ┌─────────────────────┐
    │ [Update Success?]   │
    └───┬─────────────┬───┘
        │ Yes         │ No
        ↓             ↓
    Show Success   Show Error
        │             │
        └─────┬───────┘
              ↓
    ┌─────────────────────┐
    │ Upload Data?         │
    └──────────┬──────────┘
               ↓
         Upload File
               ↓
    ┌─────────────────────┐
    │ [File Valid?]        │
    └───┬─────────────┬───┘
        │ Yes         │ No
        ↓             ↓
    Process File   Show Error
        │             │
        └─────┬───────┘
              ↓
    ┌─────────────────────┐
    │ Logout?              │
    └──────────┬──────────┘
               ↓
         Clear Session
               ↓
         [Final]
```

---

## READY-TO-USE COMPLETE PROMPT

**Copy this entire prompt:**

```
Create a comprehensive UML Activity Diagram for Admin Dashboard user activities in the University of Ibadan ID Card Collection Status Tracker system.

SWIMLANES:
1. Admin User
2. Web Browser
3. Flask Application
4. Database

ACTIVITIES:

1. Access Dashboard
   - Admin navigates to dashboard
   - System displays statistics and student table

2. View Statistics
   - Display total students
   - Display status counts (Not Yet Printed, Printing, Ready, Collected)

3. Search Students
   - Admin enters search term
   - System filters table in real-time
   - [Decision: Results Found?]
     - Yes → Display filtered rows
     - No → Show "No results" message

4. Filter Students
   - Admin selects status filter
   - Admin selects department filter
   - System applies filters
   - [Decision: Results Found?]
     - Yes → Display filtered rows
     - No → Show "No results" message

5. Update Student Status
   - Admin selects new status from dropdown
   - System sends AJAX request
   - System updates database
   - [Decision: Update Successful?]
     - Yes → Show success toast, update badge, refresh stats
     - No → Show error, reset dropdown

6. Upload Bulk Data
   - Admin clicks "Upload Data"
   - Admin selects CSV/Excel file
   - Admin uploads file
   - [Decision: File Valid?]
     - Yes → Process file, update database
       - [Decision: Processing Successful?]
         - Yes → Show success, redirect to dashboard
         - No → Show error, rollback
     - No → Show file format error

7. Logout
   - Admin clicks "Logout"
   - System clears session
   - System redirects to homepage

PARALLEL ACTIVITIES:
- Statistics calculation runs parallel with table display
- Multiple status updates can be processed independently

DIAGRAM SPECIFICATIONS:
- Use standard UML Activity Diagram notation
- Initial node: Filled circle
- Activities: Rounded rectangles
- Decisions: Diamonds with guards [Yes/No], [Success/Error], [Valid/Invalid]
- Fork/Join: Horizontal bars for parallel activities
- Final nodes: Filled circle with ring
- Swimlanes: Four lanes separating user, browser, application, database
- Control flows: Arrows with guards where needed
- Professional layout suitable for academic documentation

Generate a complete Activity Diagram with all activities, decisions, and swimlanes.
```

---

## HOW TO USE

### In Miro AI:
1. Open Miro board
2. Click AI icon or press `/` and type "AI"
3. Select "Generate diagram" or "Create with AI"
4. Paste the complete prompt above
5. Click Generate
6. Customize activities, decisions, and swimlanes as needed

### In Other Tools:
- **Draw.io**: Use prompt to get description, then create manually
- **Lucidchart**: Use AI feature with the prompt
- **PlantUML**: Ask AI to convert to PlantUML code first
- **Visual Paradigm**: Use the prompt in their AI assistant

---

## FOLLOW-UP PROMPTS

After generating, refine with:

- "Add more detail to the file upload process showing row-by-row processing"
- "Show parallel activities more clearly with fork/join nodes"
- "Add error handling flows for all decision points"
- "Expand the search/filter activities to show individual filter types"
- "Add timing constraints to show real-time updates"
- "Show the AJAX request flow in more detail"
- "Add notes explaining complex activities"

---

## TIPS FOR BEST RESULTS

1. **Be Specific**: Use the detailed prompt for better results
2. **Swimlanes**: Request swimlanes to show different layers
3. **Decisions**: Ensure all decision points have clear guards
4. **Parallel Activities**: Use fork/join nodes for parallel processing
5. **Iterate**: Generate, review, and ask for refinements

---

**This prompt is optimized for Miro AI, Draw.io, Lucidchart, PlantUML, and other UML diagramming tools!**

