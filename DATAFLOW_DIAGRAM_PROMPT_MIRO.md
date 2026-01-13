# Dataflow Diagram Prompt for Miro AI

Copy and paste this prompt directly into Miro AI to generate a dataflow diagram:

---

## PROMPT FOR MIRO AI

Create a dataflow diagram for the "University of Ibadan ID Card Collection Status Tracker" system showing how data flows through the system for different user operations.

### System Components:
1. **External Entities:**
   - Student (User)
   - ITEMS Staff (Admin)
   - File System (CSV/Excel files)

2. **Processes:**
   - Web Interface (Frontend)
   - Authentication Process
   - Search Process
   - Status Update Process
   - File Upload Process
   - Data Validation Process

3. **Data Stores:**
   - Students Database
   - Admins Database
   - Session Storage

### Data Flow Scenarios:

**Scenario 1: Student Status Check**
- Student → Matric Number → Web Interface
- Web Interface → Search Request → Search Process
- Search Process → Query → Students Database
- Students Database → Student Record → Search Process
- Search Process → Status Information → Web Interface
- Web Interface → Status Display → Student

**Scenario 2: Admin Login**
- ITEMS Staff → Credentials → Web Interface
- Web Interface → Login Request → Authentication Process
- Authentication Process → Query → Admins Database
- Admins Database → Admin Record → Authentication Process
- Authentication Process → Session Token → Session Storage
- Authentication Process → Access Granted → Web Interface
- Web Interface → Dashboard → ITEMS Staff

**Scenario 3: Admin Status Update**
- ITEMS Staff → Status Change → Web Interface
- Web Interface → Update Request → Status Update Process
- Status Update Process → Validation → Data Validation Process
- Data Validation Process → Valid → Status Update Process
- Status Update Process → Update Query → Students Database
- Students Database → Confirmation → Status Update Process
- Status Update Process → Success Message → Web Interface
- Web Interface → Updated Status → ITEMS Staff

**Scenario 4: Bulk File Upload**
- ITEMS Staff → CSV/Excel File → Web Interface
- Web Interface → File Upload → File Upload Process
- File Upload Process → File Data → File System
- File Upload Process → Read File → Data Validation Process
- Data Validation Process → Validated Records → File Upload Process
- File Upload Process → Batch Insert/Update → Students Database
- Students Database → Confirmation → File Upload Process
- File Upload Process → Success Count → Web Interface
- Web Interface → Upload Confirmation → ITEMS Staff

### Diagram Requirements:
- Use standard dataflow diagram notation (DFD)
- Show external entities as rectangles
- Show processes as circles/rounded rectangles
- Show data stores as open rectangles (two parallel lines)
- Use arrows to show data flow direction
- Label all data flows clearly
- Use different colors for different user types (Student flows vs Admin flows)
- Include process numbers (1.0, 2.0, 3.0, etc.)
- Show data store numbers (D1, D2, D3, etc.)
- Keep it clear and easy to follow
- Make it suitable for academic project documentation

Generate a Level 0 (Context Diagram) and Level 1 (Detailed Dataflow Diagram) showing all the processes and data flows described above.

---

## ALTERNATIVE: SIMPLIFIED PROMPT

**Quick Version for Miro AI:**

```
Create a dataflow diagram for an ID Card Tracker system with these flows:

1. Student checks status: Student → Web → Search Process → Database → Results → Student

2. Admin logs in: Admin → Web → Auth Process → Admin DB → Session → Dashboard → Admin

3. Admin updates status: Admin → Web → Update Process → Validation → Student DB → Confirmation → Admin

4. Admin uploads file: Admin → Web → Upload Process → File Processing → Validation → Student DB → Confirmation → Admin

Show external entities (Student, Admin), processes (Search, Auth, Update, Upload, Validation), and data stores (Student DB, Admin DB, Session). Use standard DFD notation with clear labels and arrows.
```

---

## HOW TO USE IN MIRO

### Step-by-Step Instructions:

1. **Open Miro**: Go to https://miro.com and create a new board

2. **Access Miro AI**:
   - Click on the AI icon in the toolbar (or press `/` and type "AI")
   - Select "Generate diagram" or "Create with AI"

3. **Paste the Prompt**:
   - Copy the full prompt above (between "PROMPT FOR MIRO AI" and the separator)
   - Paste it into Miro AI's prompt box

4. **Generate**:
   - Click "Generate" or press Enter
   - Miro AI will create the dataflow diagram automatically

5. **Customize**:
   - Edit colors, shapes, and labels as needed
   - Add more details if required
   - Rearrange elements for better clarity

6. **Export**:
   - Export as PNG, PDF, or SVG for your documentation

---

## TIPS FOR BEST RESULTS

1. **Be Specific**: Use the detailed prompt for better results
2. **Iterate**: If the first result isn't perfect, ask Miro AI to "refine the dataflow diagram" or "add more details"
3. **Use Layers**: Create separate layers for different scenarios if needed
4. **Add Labels**: Ensure all data flows are clearly labeled
5. **Color Code**: Use different colors for Student flows (blue) and Admin flows (green/red)

---

## FOLLOW-UP PROMPTS FOR MIRO AI

After generating the initial diagram, you can use these:

- "Add process numbers to each process (1.0, 2.0, 3.0, etc.)"
- "Add data store numbers (D1, D2, D3, etc.)"
- "Create a Level 0 context diagram showing the system as a single process"
- "Expand the file upload process to show more detail"
- "Add error handling flows to the diagram"
- "Create separate diagrams for each user type (Student flow and Admin flow)"
- "Add database query details to the data flows"

---

## EXAMPLE: COMPLETE PROMPT FOR COPY-PASTE

```
Create a comprehensive dataflow diagram for the University of Ibadan ID Card Collection Status Tracker system.

External Entities:
- Student
- ITEMS Staff (Admin)

Processes:
1. Web Interface (Frontend)
2. Authentication Process
3. Search Process
4. Status Update Process
5. File Upload Process
6. Data Validation Process

Data Stores:
- D1: Students Database (contains: matric_number, name, department, status, timestamps)
- D2: Admins Database (contains: username, password, email, timestamps)
- D3: Session Storage (contains: session tokens, user sessions)

Data Flows:

FLOW 1 - Student Status Check:
Student → "Matric Number" → Web Interface
Web Interface → "Search Request" → Search Process
Search Process → "Query by Matric" → D1: Students Database
D1: Students Database → "Student Record" → Search Process
Search Process → "Status Information" → Web Interface
Web Interface → "Status Display" → Student

FLOW 2 - Admin Login:
ITEMS Staff → "Username & Password" → Web Interface
Web Interface → "Login Request" → Authentication Process
Authentication Process → "Verify Credentials" → D2: Admins Database
D2: Admins Database → "Admin Record" → Authentication Process
Authentication Process → "Create Session" → D3: Session Storage
Authentication Process → "Access Granted" → Web Interface
Web Interface → "Dashboard" → ITEMS Staff

FLOW 3 - Admin Status Update:
ITEMS Staff → "New Status & Student ID" → Web Interface
Web Interface → "Update Request" → Status Update Process
Status Update Process → "Validate Data" → Data Validation Process
Data Validation Process → "Validation Result" → Status Update Process
Status Update Process → "Update Query" → D1: Students Database
D1: Students Database → "Update Confirmation" → Status Update Process
Status Update Process → "Success Message" → Web Interface
Web Interface → "Updated Status" → ITEMS Staff

FLOW 4 - Bulk File Upload:
ITEMS Staff → "CSV/Excel File" → Web Interface
Web Interface → "File Upload" → File Upload Process
File Upload Process → "Read File Data" → Data Validation Process
Data Validation Process → "Validated Records" → File Upload Process
File Upload Process → "Batch Insert/Update" → D1: Students Database
D1: Students Database → "Confirmation" → File Upload Process
File Upload Process → "Success Count" → Web Interface
Web Interface → "Upload Confirmation" → ITEMS Staff

Use standard DFD notation:
- External entities as rectangles
- Processes as circles with numbers (1.0, 2.0, etc.)
- Data stores as open rectangles with labels (D1, D2, D3)
- Data flows as labeled arrows
- Use color coding: Blue for Student flows, Green for Admin flows
- Make it clear and professional for academic documentation
```

---

**Ready to use!** Just copy the complete prompt above and paste it into Miro AI.

