# Architecture Diagram Generation Prompt

Copy and paste this prompt to generate a simple architecture diagram for the ID Card Tracker system:

---

## PROMPT START

Generate a simple, clear architecture diagram for the "University of Ibadan ID Card Collection Status Tracker" system.

### System Overview:
A web-based application with the following components:

**Frontend Layer:**
- Web Browser (Client)
- HTML5/CSS3/JavaScript
- Bootstrap 5 UI Framework
- Responsive design for mobile and desktop

**Application Layer:**
- Flask Web Server (Python)
- Flask Routes (8 endpoints):
  - Public: Homepage (/), Search (/search)
  - Admin: Login (/admin/login), Dashboard (/admin/dashboard), Upload (/admin/upload), Update Status (/admin/update_status), Logout (/admin/logout)
- Flask-Login (Authentication)
- Business Logic Layer

**Data Layer:**
- SQLite Database (default) or MySQL (optional)
- Two main tables:
  - Students table (id, matric_number, name, department, status, timestamps)
  - Admins table (id, username, password, email, timestamps)
- SQLAlchemy ORM

**External Components:**
- File Upload Processing (Pandas, OpenPyXL for CSV/Excel)
- Password Hashing (Werkzeug)

### User Types:
1. **Students** - Access public routes (search functionality)
2. **ITEMS Staff (Admin)** - Access protected admin routes (dashboard, upload, status updates)

### Data Flow:
1. Student enters matric number → Flask route processes → Database query → Returns status
2. Admin logs in → Authentication check → Access dashboard → View/manage students
3. Admin uploads CSV/Excel → File processing → Database update → Confirmation

### Diagram Requirements:
- Show three main layers: Presentation Layer, Application Layer, Data Layer
- Include user types (Students and Admins)
- Show authentication flow for admin
- Display database tables
- Indicate data flow with arrows
- Keep it simple and easy to understand
- Use standard architecture diagram notation

Generate this as:
- A Mermaid diagram code, OR
- A PlantUML diagram code, OR
- A detailed text description that can be used to create the diagram in draw.io/Visio

Make it suitable for inclusion in academic project documentation.

## PROMPT END

---

## Alternative: Quick Version

**Quick Prompt:**
```
Generate a simple 3-tier architecture diagram showing:
- Frontend: Web Browser with Bootstrap UI
- Backend: Flask Application with Routes and Authentication
- Database: SQLite/MySQL with Students and Admins tables
- Two user types: Students (public access) and Admins (authenticated)
- Show data flow between layers
Output as Mermaid or PlantUML code.
```

---

## Usage Tips

1. **For Mermaid diagrams**: Use the prompt and ask for "Mermaid diagram code"
2. **For PlantUML**: Ask for "PlantUML sequence diagram code"
3. **For draw.io**: Ask for "detailed description for draw.io"
4. **For text description**: Ask for "detailed architecture description"

## Example Follow-up Requests

After getting the initial diagram, you can request:
- "Add more details about the authentication flow"
- "Create a sequence diagram for the student search process"
- "Generate a database ERD diagram"
- "Create a deployment architecture diagram"

