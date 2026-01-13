# Database Schema Overview Diagram Prompt

Copy and paste this prompt to generate a Database Schema Diagram (ERD) for the ID Card Tracker system:

---

## PROMPT FOR MIRO AI / DIAGRAM TOOLS

Create a comprehensive Entity-Relationship Diagram (ERD) or Database Schema Diagram for the University of Ibadan ID Card Collection Status Tracker system.

### Database: id_card_tracker (SQLite/MySQL)

### Tables:

**1. students**
- Primary Key: id (INTEGER)
- Attributes:
  - id: INTEGER, Primary Key, Auto Increment
  - matric_number: VARCHAR(20), Unique, Not Null, Indexed
  - name: VARCHAR(100), Not Null
  - department: VARCHAR(100), Not Null
  - status: VARCHAR(50), Not Null, Default: 'Not Yet Printed'
  - date_created: DATETIME, Default: CURRENT_TIMESTAMP
  - date_updated: DATETIME, Default: CURRENT_TIMESTAMP, On Update: CURRENT_TIMESTAMP

**Constraints:**
- PRIMARY KEY: id
- UNIQUE: matric_number
- INDEX: matric_number
- CHECK: status IN ('Not Yet Printed', 'Printing in Progress', 'Ready for Pickup', 'Collected')

**2. admins**
- Primary Key: id (INTEGER)
- Attributes:
  - id: INTEGER, Primary Key, Auto Increment
  - username: VARCHAR(80), Unique, Not Null
  - password: VARCHAR(120), Not Null (Hashed)
  - email: VARCHAR(120), Unique, Nullable
  - full_name: VARCHAR(100), Nullable
  - date_created: DATETIME, Default: CURRENT_TIMESTAMP
  - last_login: DATETIME, Nullable

**Constraints:**
- PRIMARY KEY: id
- UNIQUE: username
- UNIQUE: email

### Relationships:
- No direct foreign key relationships between tables
- Both tables are independent entities managed by the same system
- Students table stores student ID card information
- Admins table stores ITEMS staff authentication information

### Diagram Specifications:
- Use standard ERD notation (Chen notation or Crow's Foot notation)
- Show entities as rectangles
- Show attributes as ovals or listed within entity boxes
- Show primary keys with underline or (PK) notation
- Show unique constraints with (UQ) notation
- Show not null constraints with (NN) notation
- Show data types for all attributes
- Show default values where applicable
- Use appropriate cardinality notation if showing relationships
- Include table names, attribute names, and constraints
- Professional appearance suitable for academic documentation

Generate a comprehensive Database Schema Diagram showing all tables, attributes, data types, and constraints.

---

## ALTERNATIVE: SIMPLIFIED PROMPT

**Quick Version:**

```
Create a database schema diagram (ERD) for an ID Card Tracker system.

Tables:
1. students (id PK, matric_number UQ NN, name NN, department NN, status NN, date_created, date_updated)
2. admins (id PK, username UQ NN, password NN, email UQ, full_name, date_created, last_login)

Show all attributes with data types, primary keys, unique constraints, and not null constraints.
Use standard ERD notation.
```

---

## DETAILED PROMPT WITH ALL DETAILS

**Complete Version for Best Results:**

```
Create a comprehensive Entity-Relationship Diagram (ERD) or Database Schema Diagram for the University of Ibadan ID Card Collection Status Tracker system.

DATABASE INFORMATION:
- Database Name: id_card_tracker
- Database Type: SQLite (can be MySQL/PostgreSQL)
- Total Tables: 2

TABLE 1: students
Description: Stores student information and ID card collection status

Attributes:
1. id
   - Data Type: INTEGER
   - Constraint: PRIMARY KEY, AUTO INCREMENT
   - Description: Unique identifier for each student record

2. matric_number
   - Data Type: VARCHAR(20)
   - Constraint: UNIQUE, NOT NULL, INDEXED
   - Description: Student's matriculation number (6 digits, e.g., "222486")
   - Example: "222486", "123456"

3. name
   - Data Type: VARCHAR(100)
   - Constraint: NOT NULL
   - Description: Full name of the student
   - Example: "John Doe", "Odukoya Oluwabukunmi"

4. department
   - Data Type: VARCHAR(100)
   - Constraint: NOT NULL
   - Description: Student's academic department
   - Example: "Computer Science", "CSC", "Mathematics"

5. status
   - Data Type: VARCHAR(50)
   - Constraint: NOT NULL, DEFAULT: 'Not Yet Printed'
   - Description: Current ID card collection status
   - Possible Values:
     * 'Not Yet Printed'
     * 'Printing in Progress'
     * 'Ready for Pickup'
     * 'Collected'

6. date_created
   - Data Type: DATETIME
   - Constraint: DEFAULT: CURRENT_TIMESTAMP
   - Description: Timestamp when record was created
   - Format: YYYY-MM-DD HH:MM:SS

7. date_updated
   - Data Type: DATETIME
   - Constraint: DEFAULT: CURRENT_TIMESTAMP, ON UPDATE: CURRENT_TIMESTAMP
   - Description: Timestamp when record was last updated
   - Format: YYYY-MM-DD HH:MM:SS

Primary Key: id
Unique Constraints: matric_number
Indexes: matric_number (for fast search)
Check Constraints: status must be one of the four valid values

TABLE 2: admins
Description: Stores ITEMS staff authentication information

Attributes:
1. id
   - Data Type: INTEGER
   - Constraint: PRIMARY KEY, AUTO INCREMENT
   - Description: Unique identifier for each admin record

2. username
   - Data Type: VARCHAR(80)
   - Constraint: UNIQUE, NOT NULL
   - Description: Admin login username
   - Example: "admin", "items_staff"

3. password
   - Data Type: VARCHAR(120)
   - Constraint: NOT NULL
   - Description: Hashed password (using Werkzeug password hashing)
   - Note: Stored as hash, not plain text

4. email
   - Data Type: VARCHAR(120)
   - Constraint: UNIQUE, NULLABLE
   - Description: Admin email address (optional)
   - Example: "admin@ui.edu.ng"

5. full_name
   - Data Type: VARCHAR(100)
   - Constraint: NULLABLE
   - Description: Full name of admin staff (optional)
   - Example: "John Smith"

6. date_created
   - Data Type: DATETIME
   - Constraint: DEFAULT: CURRENT_TIMESTAMP
   - Description: Timestamp when admin account was created
   - Format: YYYY-MM-DD HH:MM:SS

7. last_login
   - Data Type: DATETIME
   - Constraint: NULLABLE
   - Description: Timestamp of last successful login
   - Format: YYYY-MM-DD HH:MM:SS
   - Note: Updated on each login

Primary Key: id
Unique Constraints: username, email
Foreign Keys: None

RELATIONSHIPS:
- No direct foreign key relationships between students and admins tables
- Both tables are independent entities
- Students table: Managed by ITEMS staff through admin interface
- Admins table: Used for authentication and authorization
- Relationship is implicit: Admins manage Students through application logic

DIAGRAM SPECIFICATIONS:
- Use standard ERD notation (Chen notation preferred, or Crow's Foot notation)
- Entities: Rectangles with table names
- Attributes: Listed within entity boxes or as ovals connected to entities
- Primary Keys: Underlined or marked with (PK)
- Unique Attributes: Marked with (UQ) or unique symbol
- Not Null Attributes: Marked with (NN) or asterisk (*)
- Nullable Attributes: Marked with (O) or left unmarked
- Data Types: Shown for all attributes
- Default Values: Shown in parentheses or notes
- Constraints: Shown clearly (PRIMARY KEY, UNIQUE, NOT NULL, INDEX)
- Use appropriate colors: Different color for each table
- Include legend explaining notation
- Professional layout suitable for academic documentation

ADDITIONAL INFORMATION TO DISPLAY:
- Table descriptions
- Sample data types and formats
- Constraint explanations
- Index information
- Default values
- Possible values for status field

Generate a comprehensive Database Schema Diagram with all details.
```

---

## VISUAL LAYOUT DESCRIPTION

**For Better Understanding:**

```
┌─────────────────────────────────────┐
│         students                    │
├─────────────────────────────────────┤
│ id (PK) INTEGER                     │
│ matric_number (UQ, NN, IDX) VARCHAR │
│ name (NN) VARCHAR(100)              │
│ department (NN) VARCHAR(100)        │
│ status (NN, DEF) VARCHAR(50)        │
│   Values:                           │
│   - Not Yet Printed                 │
│   - Printing in Progress           │
│   - Ready for Pickup                │
│   - Collected                       │
│ date_created (DEF) DATETIME         │
│ date_updated (DEF, ON UPDATE) DATET │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│         admins                      │
├─────────────────────────────────────┤
│ id (PK) INTEGER                     │
│ username (UQ, NN) VARCHAR(80)       │
│ password (NN) VARCHAR(120) [Hashed] │
│ email (UQ) VARCHAR(120)             │
│ full_name VARCHAR(100)              │
│ date_created (DEF) DATETIME         │
│ last_login DATETIME                 │
└─────────────────────────────────────┘
```

---

## READY-TO-USE COMPLETE PROMPT

**Copy this entire prompt:**

```
Create a comprehensive Entity-Relationship Diagram (ERD) or Database Schema Diagram for the University of Ibadan ID Card Collection Status Tracker system.

DATABASE: id_card_tracker

TABLE 1: students
Description: Stores student information and ID card collection status

Attributes:
- id: INTEGER, PRIMARY KEY, AUTO INCREMENT
- matric_number: VARCHAR(20), UNIQUE, NOT NULL, INDEXED
- name: VARCHAR(100), NOT NULL
- department: VARCHAR(100), NOT NULL
- status: VARCHAR(50), NOT NULL, DEFAULT: 'Not Yet Printed'
  Possible Values: 'Not Yet Printed', 'Printing in Progress', 'Ready for Pickup', 'Collected'
- date_created: DATETIME, DEFAULT: CURRENT_TIMESTAMP
- date_updated: DATETIME, DEFAULT: CURRENT_TIMESTAMP, ON UPDATE: CURRENT_TIMESTAMP

Constraints:
- PRIMARY KEY: id
- UNIQUE: matric_number
- INDEX: matric_number

TABLE 2: admins
Description: Stores ITEMS staff authentication information

Attributes:
- id: INTEGER, PRIMARY KEY, AUTO INCREMENT
- username: VARCHAR(80), UNIQUE, NOT NULL
- password: VARCHAR(120), NOT NULL (Hashed using Werkzeug)
- email: VARCHAR(120), UNIQUE, NULLABLE
- full_name: VARCHAR(100), NULLABLE
- date_created: DATETIME, DEFAULT: CURRENT_TIMESTAMP
- last_login: DATETIME, NULLABLE

Constraints:
- PRIMARY KEY: id
- UNIQUE: username, email

RELATIONSHIPS:
- No direct foreign key relationships
- Both tables are independent entities
- Admins manage Students through application logic (no database-level relationship)

DIAGRAM SPECIFICATIONS:
- Use standard ERD notation (Chen notation or Crow's Foot)
- Entities: Rectangles with table names
- Attributes: Listed within entity boxes
- Primary Keys: Underlined or marked with (PK)
- Unique: Marked with (UQ)
- Not Null: Marked with (NN) or asterisk
- Data Types: Shown for all attributes
- Default Values: Shown in parentheses
- Include constraint information
- Use different colors for each table
- Include legend explaining notation
- Professional layout suitable for academic documentation

Generate a comprehensive Database Schema Diagram with all tables, attributes, data types, constraints, and relationships.
```

---

## ALTERNATIVE: TABLE-FORMAT SCHEMA DIAGRAM

**For a more tabular representation:**

```
Create a database schema overview diagram showing tables in a tabular format.

TABLE: students
┌─────────────────┬──────────────┬─────────────┬─────────────────────────────┐
│ Attribute       │ Data Type    │ Constraints │ Description                 │
├─────────────────┼──────────────┼─────────────┼─────────────────────────────┤
│ id              │ INTEGER      │ PK, AI      │ Primary key                 │
│ matric_number  │ VARCHAR(20)  │ UQ, NN, IDX │ Unique matric number       │
│ name            │ VARCHAR(100) │ NN          │ Student name                │
│ department     │ VARCHAR(100) │ NN          │ Department                  │
│ status          │ VARCHAR(50)  │ NN, DEF     │ ID card status             │
│ date_created    │ DATETIME     │ DEF         │ Creation timestamp         │
│ date_updated    │ DATETIME     │ DEF, ON UP  │ Last update timestamp      │
└─────────────────┴──────────────┴─────────────┴─────────────────────────────┘

TABLE: admins
┌──────────────┬──────────────┬─────────────┬─────────────────────────────┐
│ Attribute    │ Data Type    │ Constraints │ Description                 │
├──────────────┼──────────────┼─────────────┼─────────────────────────────┤
│ id           │ INTEGER      │ PK, AI      │ Primary key                 │
│ username     │ VARCHAR(80)  │ UQ, NN      │ Login username              │
│ password     │ VARCHAR(120) │ NN          │ Hashed password             │
│ email        │ VARCHAR(120) │ UQ          │ Email address               │
│ full_name    │ VARCHAR(100) │             │ Admin full name             │
│ date_created │ DATETIME     │ DEF         │ Account creation time       │
│ last_login   │ DATETIME     │             │ Last login timestamp        │
└──────────────┴──────────────┴─────────────┴─────────────────────────────┘

Show this in a clear, professional diagram format suitable for documentation.
```

---

## HOW TO USE

### In Miro AI:
1. Open Miro board
2. Click AI icon or press `/` and type "AI"
3. Select "Generate diagram" or "Create with AI"
4. Paste the complete prompt above
5. Click Generate
6. Customize tables, attributes, and relationships as needed

### In Other Tools:
- **Draw.io**: Use prompt to get description, then create manually
- **Lucidchart**: Use AI feature with the prompt
- **dbdiagram.io**: Perfect for database schemas - use the prompt
- **PlantUML**: Ask AI to convert to PlantUML code first
- **MySQL Workbench**: Use for reverse engineering or forward engineering

---

## FOLLOW-UP PROMPTS

After generating, refine with:

- "Add data type sizes (VARCHAR lengths) to all attributes"
- "Show default values more prominently"
- "Add sample data examples for each attribute"
- "Include index information in the diagram"
- "Add check constraints for the status field"
- "Show nullable vs not null attributes more clearly"
- "Add table descriptions as notes"
- "Create a separate diagram showing relationships if any are added"

---

## TIPS FOR BEST RESULTS

1. **Be Specific**: Use the detailed prompt for better results
2. **Notation**: Specify Chen notation or Crow's Foot notation preference
3. **Details**: Include all constraints, data types, and defaults
4. **Layout**: Request specific positioning (students on left, admins on right)
5. **Colors**: Ask for different colors for each table
6. **Legend**: Request a legend explaining notation symbols

---

## SPECIALIZED TOOLS FOR DATABASE SCHEMAS

**Recommended Tools:**
1. **dbdiagram.io** - Excellent for database schemas
2. **MySQL Workbench** - For MySQL-specific schemas
3. **pgAdmin** - For PostgreSQL schemas
4. **Lucidchart** - Good ERD support
5. **Draw.io** - Free and versatile

---

**This prompt is optimized for Miro AI, Draw.io, Lucidchart, dbdiagram.io, PlantUML, and other database diagramming tools!**

