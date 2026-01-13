# Use Case Diagram Prompt

Copy and paste this prompt to generate a Use Case Diagram for the ID Card Tracker system:

---

## PROMPT FOR MIRO AI / DIAGRAM TOOLS

Create a Use Case Diagram for the "University of Ibadan ID Card Collection Status Tracker" system using standard UML notation.

### Actors:
1. **Student** (Primary Actor - shown as stick figure on left)
2. **ITEMS Staff** (Primary Actor - shown as stick figure on right)
3. **System** (Secondary Actor - optional, shown as rectangle if needed)

### Use Cases:

**Student Use Cases:**
1. Check ID Card Status
2. View Status Details
3. Search by Matric Number

**ITEMS Staff Use Cases:**
1. Login to System
2. View Dashboard
3. View All Students
4. Search Students
5. Update Student Status
6. Upload Bulk Data File
7. Process CSV/Excel File
8. Logout from System

### Relationships:

**Student Actor:**
- Student → (uses) → Check ID Card Status
- Check ID Card Status → (includes) → Search by Matric Number
- Check ID Card Status → (includes) → View Status Details

**ITEMS Staff Actor:**
- ITEMS Staff → (uses) → Login to System
- ITEMS Staff → (uses) → View Dashboard
- ITEMS Staff → (uses) → View All Students
- ITEMS Staff → (uses) → Search Students
- ITEMS Staff → (uses) → Update Student Status
- ITEMS Staff → (uses) → Upload Bulk Data File
- ITEMS Staff → (uses) → Logout from System
- Upload Bulk Data File → (includes) → Process CSV/Excel File
- View Dashboard → (extends) → View All Students (optional)

### Diagram Specifications:
- Use standard UML Use Case Diagram notation
- Actors as stick figures or rectangles with <<actor>> stereotype
- Use cases as ovals/ellipses
- Association lines (solid lines) between actors and use cases
- Include relationship (dashed arrow with <<include>>)
- Extend relationship (dashed arrow with <<extend>>) where applicable
- System boundary rectangle (optional) labeled "ID Card Tracker System"
- Clear, readable labels
- Professional appearance for academic documentation

Generate a comprehensive Use Case Diagram following UML standards.

---

## ALTERNATIVE: SIMPLIFIED PROMPT

**Quick Version:**

```
Create a Use Case Diagram for an ID Card Tracker system.

Actors:
- Student
- ITEMS Staff

Use Cases:
Student: Check Status, Search by Matric, View Details
ITEMS Staff: Login, View Dashboard, View Students, Search, Update Status, Upload File, Logout

Relationships:
- Check Status includes Search by Matric and View Details
- Upload File includes Process File
- Use standard UML notation with actors, use cases, and relationships.
```

---

## DETAILED PROMPT WITH ALL USE CASES

**Complete Version for Best Results:**

```
Create a comprehensive Use Case Diagram for the University of Ibadan ID Card Collection Status Tracker system using standard UML notation.

ACTORS:
1. Student (Primary Actor - stick figure on left side)
2. ITEMS Staff / Admin (Primary Actor - stick figure on right side)

USE CASES:

For Student Actor:
1. "Check ID Card Status" (main use case)
2. "Search by Matric Number" (included use case)
3. "View Status Details" (included use case)

For ITEMS Staff Actor:
1. "Login to System" (authentication use case)
2. "View Dashboard" (main use case)
3. "View All Students" (main use case)
4. "Search Students" (main use case)
5. "Update Student Status" (main use case)
6. "Upload Bulk Data File" (main use case)
7. "Process CSV/Excel File" (included use case)
8. "Logout from System" (main use case)

RELATIONSHIPS:

Include Relationships (<<include>>):
- "Check ID Card Status" includes "Search by Matric Number"
- "Check ID Card Status" includes "View Status Details"
- "Upload Bulk Data File" includes "Process CSV/Excel File"

Association Relationships:
- Student is associated with "Check ID Card Status"
- ITEMS Staff is associated with all ITEMS Staff use cases

Dependencies (optional):
- "View Dashboard" may extend "View All Students" (if showing all students on dashboard)
- "Update Student Status" requires "View All Students" or "Search Students" (precondition)

SYSTEM BOUNDARY:
- Draw a rectangle labeled "ID Card Collection Status Tracker System" enclosing all use cases

DIAGRAM LAYOUT:
- Place Student actor on the left
- Place ITEMS Staff actor on the right
- Group Student use cases on the left side
- Group ITEMS Staff use cases on the right side
- System boundary rectangle around all use cases
- Use standard UML notation

STYLING:
- Actors: Stick figures or rectangles with <<actor>> stereotype
- Use cases: Ovals/ellipses with descriptive names
- Association: Solid lines from actors to use cases
- Include: Dashed arrow with <<include>> label
- Extend: Dashed arrow with <<extend>> label (if used)
- Clear, readable text
- Professional appearance suitable for academic documentation

Generate a complete Use Case Diagram following UML 2.0 standards.
```

---

## VISUAL LAYOUT DESCRIPTION

**For Better Understanding:**

```
                    [Student]
                        |
                        | (association)
                        ↓
        ┌─────────────────────────────────────┐
        │  ID Card Tracker System             │
        │                                     │
        │  (Check ID Card Status)             │
        │         ↑                           │
        │         | <<include>>               │
        │  (Search by Matric)  (View Details) │
        │                                     │
        │  (Login)  (View Dashboard)          │
        │  (View All Students)                │
        │  (Search Students)                  │
        │  (Update Status)                    │
        │  (Upload File) → <<include>> →      │
        │  (Process File)                     │
        │  (Logout)                           │
        │                                     │
        └─────────────────────────────────────┘
                        ↑
                        | (associations)
                        |
                [ITEMS Staff]
```

---

## DETAILED USE CASE DESCRIPTIONS

**For Reference (can be included in prompt):**

```
Use Case Details:

STUDENT USE CASES:
1. Check ID Card Status
   - Description: Student checks their ID card collection status
   - Includes: Search by Matric Number, View Status Details
   - Precondition: Student has matric number
   - Postcondition: Student sees their status

2. Search by Matric Number
   - Description: System searches database using matric number
   - Included in: Check ID Card Status

3. View Status Details
   - Description: Display student's status, name, department, last update
   - Included in: Check ID Card Status

ITEMS STAFF USE CASES:
1. Login to System
   - Description: ITEMS staff authenticates to access admin features
   - Precondition: Staff has valid credentials
   - Postcondition: Staff is logged in

2. View Dashboard
   - Description: View overview of all students and statistics
   - Precondition: Staff is logged in

3. View All Students
   - Description: Display list of all student records
   - Precondition: Staff is logged in

4. Search Students
   - Description: Search for specific students by name or matric
   - Precondition: Staff is logged in

5. Update Student Status
   - Description: Change a student's ID card status
   - Precondition: Staff is logged in, student record exists
   - Postcondition: Student status is updated

6. Upload Bulk Data File
   - Description: Upload CSV/Excel file with student data
   - Includes: Process CSV/Excel File
   - Precondition: Staff is logged in, file is valid format
   - Postcondition: Students are added/updated in database

7. Process CSV/Excel File
   - Description: System processes uploaded file and validates data
   - Included in: Upload Bulk Data File

8. Logout from System
   - Description: ITEMS staff logs out of the system
   - Precondition: Staff is logged in
   - Postcondition: Staff session is terminated
```

---

## READY-TO-USE COMPLETE PROMPT

**Copy this entire prompt:**

```
Create a comprehensive Use Case Diagram for the University of Ibadan ID Card Collection Status Tracker system using standard UML 2.0 notation.

ACTORS:
1. Student (Primary Actor - stick figure, positioned left)
2. ITEMS Staff (Primary Actor - stick figure, positioned right)

USE CASES:

Student Use Cases:
- Check ID Card Status (main use case)
- Search by Matric Number (included use case)
- View Status Details (included use case)

ITEMS Staff Use Cases:
- Login to System
- View Dashboard
- View All Students
- Search Students
- Update Student Status
- Upload Bulk Data File
- Process CSV/Excel File (included use case)
- Logout from System

RELATIONSHIPS:

Include Relationships (<<include>>):
- "Check ID Card Status" includes "Search by Matric Number"
- "Check ID Card Status" includes "View Status Details"
- "Upload Bulk Data File" includes "Process CSV/Excel File"

Associations:
- Student → Check ID Card Status
- ITEMS Staff → Login to System
- ITEMS Staff → View Dashboard
- ITEMS Staff → View All Students
- ITEMS Staff → Search Students
- ITEMS Staff → Update Student Status
- ITEMS Staff → Upload Bulk Data File
- ITEMS Staff → Logout from System

SYSTEM BOUNDARY:
- Rectangle labeled "ID Card Collection Status Tracker System" enclosing all use cases

DIAGRAM SPECIFICATIONS:
- Use standard UML Use Case Diagram notation
- Actors: Stick figures or rectangles with <<actor>> stereotype
- Use cases: Ovals/ellipses
- Association: Solid lines from actors to use cases
- Include: Dashed arrows with <<include>> label pointing from including to included use case
- System boundary: Rectangle around all use cases
- Clear, readable labels
- Professional layout: Student use cases on left, ITEMS Staff use cases on right
- Suitable for academic project documentation

Generate a complete, professional Use Case Diagram.
```

---

## HOW TO USE

### In Miro AI:
1. Open Miro board
2. Click AI icon or press `/` and type "AI"
3. Select "Generate diagram" or "Create with AI"
4. Paste the complete prompt above
5. Click Generate
6. Customize actors, use cases, and relationships as needed

### In Other Tools:
- **Draw.io**: Use prompt to get description, then create manually
- **Lucidchart**: Use AI feature with the prompt
- **PlantUML**: Ask AI to convert to PlantUML code first
- **Visual Paradigm**: Use the prompt in their AI assistant

---

## FOLLOW-UP PROMPTS

After generating, refine with:

- "Add use case descriptions below each use case"
- "Add system boundary rectangle around all use cases"
- "Make the include relationships more prominent"
- "Add generalization if Student and ITEMS Staff share common use cases"
- "Add extend relationships where applicable"
- "Create separate diagrams for Student use cases and Admin use cases"

---

## TIPS FOR BEST RESULTS

1. **Be Specific**: Use the detailed prompt for better results
2. **Iterate**: Generate, review, and ask for refinements
3. **Layout**: Request specific positioning (Student left, ITEMS Staff right)
4. **Relationships**: Ensure include relationships are clearly shown
5. **Labels**: Make sure all use cases and actors are clearly labeled

---

**This prompt is optimized for Miro AI, Draw.io, Lucidchart, and other UML diagramming tools!**

