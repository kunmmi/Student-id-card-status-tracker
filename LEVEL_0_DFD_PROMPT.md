# Level 0 DFD (Context Diagram) Prompt

Copy and paste this prompt to generate a Level 0 DFD for the ID Card Tracker system:

---

## PROMPT FOR MIRO AI / DIAGRAM TOOLS

Create a Level 0 Data Flow Diagram (Context Diagram) for the "University of Ibadan ID Card Collection Status Tracker" system.

### Level 0 DFD Requirements:
- Show the entire system as ONE single process (centered)
- Show all external entities around the system
- Show all data flows between external entities and the system
- Use standard DFD notation

### System Process:
**ID Card Collection Status Tracker System** (shown as one circle/process in the center)

### External Entities:
1. **Student** (shown as rectangle on the left)
2. **ITEMS Staff** (shown as rectangle on the right)
3. **File System** (shown as rectangle at the bottom, optional)

### Data Flows:

**From Student to System:**
- "Matric Number" (input for status check)

**From System to Student:**
- "ID Card Status Information" (output showing status, name, department, last update)

**From ITEMS Staff to System:**
- "Login Credentials" (username and password)
- "Status Update Request" (student ID and new status)
- "Bulk Upload File" (CSV/Excel file with student data)

**From System to ITEMS Staff:**
- "Authentication Response" (login success/failure)
- "Student Records" (dashboard data, search results)
- "Update Confirmation" (status update success/failure)
- "Upload Confirmation" (file processing results)

### Diagram Specifications:
- System process: Large circle in center labeled "ID Card Collection Status Tracker System" or "ID Card Tracker System"
- External entities: Rectangles positioned around the system
- Data flows: Labeled arrows showing direction of data
- Use clear, readable labels
- Keep it simple - Level 0 shows only external interactions
- Use color coding: Blue for Student flows, Green for Admin flows
- Make it suitable for academic project documentation

Generate a clean, professional Level 0 Context Diagram following standard DFD notation.

---

## ALTERNATIVE: SIMPLIFIED PROMPT

**Quick Version:**

```
Create a Level 0 DFD (Context Diagram) for an ID Card Tracker system.

Show the system as ONE process in the center labeled "ID Card Tracker System".

External Entities:
- Student (left side)
- ITEMS Staff (right side)

Data Flows:
Student → System: "Matric Number"
System → Student: "Status Information"
ITEMS Staff → System: "Credentials", "Update Requests", "Upload Files"
System → ITEMS Staff: "Auth Response", "Student Data", "Confirmations"

Use standard DFD notation: system as circle, entities as rectangles, flows as labeled arrows.
```

---

## DETAILED PROMPT WITH ALL FLOWS

**Complete Version for Best Results:**

```
Create a Level 0 Data Flow Diagram (Context Diagram) for the University of Ibadan ID Card Collection Status Tracker system.

SYSTEM:
- Single process circle in center labeled "ID Card Collection Status Tracker System" or "ID Card Tracker System"

EXTERNAL ENTITIES (Rectangles):
1. Student (position: left side of diagram)
2. ITEMS Staff / Admin (position: right side of diagram)

DATA FLOWS (Labeled Arrows):

INCOMING FLOWS (To System):
1. From Student:
   - "Matric Number" → System (for status check)

2. From ITEMS Staff:
   - "Login Credentials" → System (username, password)
   - "Status Update Request" → System (student ID, new status)
   - "Bulk Upload File" → System (CSV/Excel file)

OUTGOING FLOWS (From System):
1. To Student:
   - System → "ID Card Status" (status, name, department, last update time)

2. To ITEMS Staff:
   - System → "Authentication Result" (login success/failure, session)
   - System → "Student Records" (dashboard data, search results, statistics)
   - System → "Update Confirmation" (status update success/failure message)
   - System → "Upload Confirmation" (file processing results, success count, errors)

DIAGRAM LAYOUT:
- System process: Large circle in the center
- Student entity: Rectangle on the left
- ITEMS Staff entity: Rectangle on the right
- All flows clearly labeled with descriptive names
- Arrows show direction of data flow
- Use standard DFD notation

STYLING:
- Use color coding: Blue arrows for Student flows, Green arrows for ITEMS Staff flows
- Keep it clean and uncluttered
- Professional appearance suitable for academic documentation
- Clear, readable text labels

Generate a Level 0 Context Diagram following these specifications.
```

---

## VISUAL LAYOUT DESCRIPTION

**For Better Results, Include This:**

```
Layout the diagram as follows:

        [Student]
            |
            | "Matric Number"
            ↓
    ┌───────────────────────┐
    │  ID Card Tracker      │
    │      System           │
    └───────────────────────┘
            ↑
            | "Status Information"
            |
        [Student]

    [ITEMS Staff] → "Credentials" → System
    [ITEMS Staff] → "Update Request" → System
    [ITEMS Staff] → "Upload File" → System
    
    System → "Auth Response" → [ITEMS Staff]
    System → "Student Records" → [ITEMS Staff]
    System → "Update Confirmation" → [ITEMS Staff]
    System → "Upload Confirmation" → [ITEMS Staff]
```

---

## HOW TO USE

### In Miro AI:
1. Open Miro board
2. Click AI icon or press `/` and type "AI"
3. Select "Generate diagram"
4. Paste the complete detailed prompt above
5. Click Generate
6. Customize as needed

### In Other Tools:
- **Draw.io**: Use the prompt to get a description, then create manually
- **Lucidchart**: Use AI feature with the prompt
- **PlantUML**: Ask AI to convert to PlantUML code first

---

## EXAMPLE OUTPUT DESCRIPTION

The Level 0 DFD should show:

```
                    [Student]
                        |
            "Matric Number"
                        ↓
        ┌──────────────────────────────┐
        │  ID Card Collection Status   │
        │      Tracker System          │
        └──────────────────────────────┘
                        ↑
            "Status Information"
                        |
                    [Student]

[ITEMS Staff] ──→ "Credentials" ──→ System
[ITEMS Staff] ──→ "Update Request" ──→ System
[ITEMS Staff] ──→ "Upload File" ──→ System

System ──→ "Auth Response" ──→ [ITEMS Staff]
System ──→ "Student Records" ──→ [ITEMS Staff]
System ──→ "Update Confirmation" ──→ [ITEMS Staff]
System ──→ "Upload Confirmation" ──→ [ITEMS Staff]
```

---

## FOLLOW-UP PROMPTS

After generating, you can refine with:

- "Add process number 0.0 to the system process"
- "Make the system process circle larger and more prominent"
- "Add color coding: blue for student flows, green for admin flows"
- "Separate the flows more clearly with better spacing"
- "Add a title 'Level 0 DFD - Context Diagram' at the top"

---

## READY-TO-USE COMPLETE PROMPT

Copy this entire prompt:

```
Create a Level 0 Data Flow Diagram (Context Diagram) for the University of Ibadan ID Card Collection Status Tracker system.

Show the entire system as ONE single process circle in the center labeled "ID Card Collection Status Tracker System".

External Entities (shown as rectangles):
1. Student (position: left side)
2. ITEMS Staff (position: right side)

Data Flows (labeled arrows):

From Student to System:
- "Matric Number" (input for status check)

From System to Student:
- "ID Card Status Information" (output: status, name, department, last update)

From ITEMS Staff to System:
- "Login Credentials" (username and password)
- "Status Update Request" (student ID and new status)
- "Bulk Upload File" (CSV/Excel file with student data)

From System to ITEMS Staff:
- "Authentication Response" (login success/failure, session token)
- "Student Records" (dashboard data, search results, statistics)
- "Update Confirmation" (status update success/failure message)
- "Upload Confirmation" (file processing results, success count)

Use standard DFD notation:
- System as large circle in center (process 0.0)
- External entities as rectangles
- Data flows as labeled arrows with clear direction
- Color code: Blue for Student flows, Green for ITEMS Staff flows
- Professional appearance suitable for academic documentation

Generate a clean, clear Level 0 Context Diagram.
```

---

**This prompt is optimized for Miro AI and other diagramming tools!**

