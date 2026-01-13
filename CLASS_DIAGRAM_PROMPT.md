# Class Diagram Prompt

Copy and paste this prompt to generate a Class Diagram for the ID Card Tracker system:

---

## PROMPT FOR MIRO AI / DIAGRAM TOOLS

Create a UML Class Diagram for the "University of Ibadan ID Card Collection Status Tracker" system using standard UML 2.0 notation.

### Classes:

**1. Student Class:**
- Attributes:
  - id: Integer (Primary Key)
  - matric_number: String (Unique, Not Null, Indexed)
  - name: String (Not Null)
  - department: String (Not Null)
  - status: String (Not Null, Default: 'Not Yet Printed')
  - date_created: DateTime (Default: datetime.utcnow)
  - date_updated: DateTime (Default: datetime.utcnow, OnUpdate)
- Methods:
  + __repr__(): String
  + to_dict(): Dictionary

**2. Admin Class:**
- Attributes:
  - id: Integer (Primary Key)
  - username: String (Unique, Not Null)
  - password: String (Not Null, Hashed)
  - email: String (Unique, Nullable)
  - full_name: String (Nullable)
  - date_created: DateTime (Default: datetime.utcnow)
  - last_login: DateTime (Nullable)
- Methods:
  + __repr__(): String
  + set_password(password: String): void
  + check_password(password: String): Boolean

**3. Flask App Class (Flask):**
- Attributes:
  - config: Dictionary
  - secret_key: String
- Methods:
  + route(path: String): Decorator
  + run(host: String, port: Integer, debug: Boolean): void

**4. Database Class (SQLAlchemy):**
- Attributes:
  - session: Session
- Methods:
  + create_all(): void
  + init_app(app: Flask): void
  + session.commit(): void
  + session.rollback(): void

**5. LoginManager Class (Flask-Login):**
- Attributes:
  - login_view: String
- Methods:
  + init_app(app: Flask): void
  + user_loader(callback: Function): void

### Relationships:

- Student and Admin both inherit from db.Model (SQLAlchemy Model)
- Admin implements UserMixin (Flask-Login interface)
- Flask App has composition relationship with Database
- Flask App has composition relationship with LoginManager
- Student and Admin are stored in the same Database (no direct relationship, but both use Database)

### Diagram Specifications:
- Use standard UML Class Diagram notation
- Classes as rectangles with three compartments: Class Name, Attributes, Methods
- Show visibility: + (public), - (private), # (protected)
- Show data types for attributes and method parameters
- Show return types for methods
- Use inheritance arrows (triangle) for inheritance relationships
- Use composition arrows (filled diamond) for composition
- Use association lines for other relationships
- Add stereotypes where appropriate (<<Model>>, <<Controller>>)
- Clear, readable labels
- Professional appearance for academic documentation

Generate a comprehensive Class Diagram following UML 2.0 standards.

---

## ALTERNATIVE: SIMPLIFIED PROMPT

**Quick Version:**

```
Create a UML Class Diagram for an ID Card Tracker system.

Classes:
1. Student (id, matric_number, name, department, status, timestamps, methods: __repr__, to_dict)
2. Admin (id, username, password, email, full_name, timestamps, methods: __repr__, set_password, check_password)
3. Flask App (config, methods: route, run)
4. Database (session, methods: create_all, init_app, commit, rollback)

Relationships:
- Student and Admin inherit from db.Model
- Admin implements UserMixin
- Flask App composes Database and LoginManager

Use standard UML notation with attributes and methods.
```

---

## DETAILED PROMPT WITH ALL CLASSES

**Complete Version for Best Results:**

```
Create a comprehensive UML Class Diagram for the University of Ibadan ID Card Collection Status Tracker system using standard UML 2.0 notation.

CLASSES:

1. Student
   Stereotype: <<Model>>
   Attributes:
   - id: Integer {Primary Key}
   - matric_number: String {Unique, Not Null, Indexed}
   - name: String {Not Null}
   - department: String {Not Null}
   - status: String {Not Null, Default = 'Not Yet Printed'}
   - date_created: DateTime {Default = datetime.utcnow}
   - date_updated: DateTime {Default = datetime.utcnow, OnUpdate}
   
   Methods:
   + __repr__(): String
   + to_dict(): Dictionary

2. Admin
   Stereotype: <<Model>>
   Attributes:
   - id: Integer {Primary Key}
   - username: String {Unique, Not Null}
   - password: String {Not Null, Hashed}
   - email: String {Unique, Nullable}
   - full_name: String {Nullable}
   - date_created: DateTime {Default = datetime.utcnow}
   - last_login: DateTime {Nullable}
   
   Methods:
   + __repr__(): String
   + set_password(password: String): void
   + check_password(password: String): Boolean

3. FlaskApp
   Stereotype: <<Controller>>
   Attributes:
   - config: Dictionary
   - secret_key: String
   - db_type: String
   
   Methods:
   + route(path: String, methods: List): Decorator
   + run(host: String, port: Integer, debug: Boolean): void
   + index(): Response
   + search(): Response
   + admin_login(): Response
   + admin_dashboard(): Response
   + admin_upload(): Response
   + update_status(): JSON
   + admin_logout(): Response
   + allowed_file(filename: String): Boolean

4. SQLAlchemy (Database)
   Stereotype: <<Database>>
   Attributes:
   - session: Session
   - engine: Engine
   
   Methods:
   + init_app(app: FlaskApp): void
   + create_all(): void
   + session.commit(): void
   + session.rollback(): void
   + query: Query

5. LoginManager
   Stereotype: <<Security>>
   Attributes:
   - login_view: String
   - app: FlaskApp
   
   Methods:
   + init_app(app: FlaskApp): void
   + user_loader(callback: Function): void
   + login_user(user: Admin): void
   + logout_user(): void
   + login_required(): Decorator

6. UserMixin (Interface)
   Stereotype: <<Interface>>
   Methods:
   + is_authenticated: Boolean
   + is_active: Boolean
   + is_anonymous: Boolean
   + get_id(): String

RELATIONSHIPS:

Inheritance (Generalization):
- Student inherits from db.Model (SQLAlchemy Model)
- Admin inherits from db.Model (SQLAlchemy Model)
- Admin implements UserMixin (Flask-Login interface)

Composition:
- FlaskApp ◄─── Database (FlaskApp contains Database)
- FlaskApp ◄─── LoginManager (FlaskApp contains LoginManager)

Dependency:
- FlaskApp depends on Student (uses Student class)
- FlaskApp depends on Admin (uses Admin class)
- LoginManager depends on Admin (manages Admin authentication)

Association:
- Database stores Student instances
- Database stores Admin instances

DIAGRAM SPECIFICATIONS:
- Use standard UML Class Diagram notation
- Classes as rectangles with three compartments:
  * Top: Class name with stereotype
  * Middle: Attributes with visibility, type, and constraints
  * Bottom: Methods with visibility, parameters, and return types
- Visibility notation: + (public), - (private), # (protected)
- Show data types: Integer, String, DateTime, Boolean, Dictionary, etc.
- Inheritance: Solid line with hollow triangle arrow (Student → db.Model)
- Implementation: Dashed line with hollow triangle arrow (Admin → UserMixin)
- Composition: Solid line with filled diamond (FlaskApp ◄─── Database)
- Dependency: Dashed arrow (FlaskApp ──→ Student)
- Association: Solid line (Database ── Student)
- Add multiplicities where appropriate (1..*, 0..1, etc.)
- Use stereotypes: <<Model>>, <<Controller>>, <<Database>>, <<Security>>, <<Interface>>
- Clear, readable labels
- Professional layout suitable for academic documentation

Generate a complete, professional Class Diagram following UML 2.0 standards.
```

---

## VISUAL LAYOUT DESCRIPTION

**For Better Understanding:**

```
┌─────────────────────┐
│   <<Interface>>     │
│    UserMixin        │
│                     │
│ + is_authenticated  │
│ + is_active         │
│ + get_id()          │
└──────────┬──────────┘
           │ (implements)
           │
┌──────────┴──────────┐      ┌──────────────────┐
│   <<Model>>        │      │   <<Model>>      │
│   db.Model         │      │   Student        │
│                    │      │                  │
│                    │      │ - id: Integer    │
│                    │      │ - matric_number  │
│                    │      │ - name: String   │
│                    │      │ - department     │
│                    │      │ - status: String │
│                    │      │ - date_created   │
│                    │      │ - date_updated   │
│                    │      │                  │
│                    │      │ + __repr__()     │
│                    │      │ + to_dict()      │
└──────────┬─────────┘      └────────┬─────────┘
           │ (inherits)              │ (inherits)
           │                          │
┌──────────┴──────────┐      ┌────────┴─────────┐
│   <<Model>>        │      │   <<Model>>      │
│   Admin            │      │   Student         │
│                    │      │                   │
│ - id: Integer      │      │ (same as above)   │
│ - username: String │      │                   │
│ - password: String │      │                   │
│ - email: String    │      │                   │
│ - full_name: String│      │                   │
│ - date_created     │      │                   │
│ - last_login       │      │                   │
│                    │      │                   │
│ + __repr__()       │      │                   │
│ + set_password()   │      │                   │
│ + check_password() │      │                   │
└──────────┬─────────┘      └───────────────────┘
           │
           │ (uses)
           │
┌──────────┴──────────┐
│  <<Controller>>     │
│  FlaskApp           │
│                     │
│ - config            │
│ - secret_key        │
│                     │
│ + route()           │
│ + run()             │
│ + index()           │
│ + search()          │
│ + admin_login()     │
│ + admin_dashboard() │
│ + admin_upload()     │
│ + update_status()   │
└──────────┬──────────┘
           │ (contains)
           │
    ┌──────┴──────┐
    │             │
┌───┴────┐  ┌─────┴──────┐
│Database│  │LoginManager│
│        │  │            │
│+init_  │  │+init_app() │
│ app()  │  │+user_      │
│+create │  │ loader()   │
│ _all() │  │+login_     │
│+commit │  │ user()     │
│()      │  │            │
└────────┘  └────────────┘
```

---

## READY-TO-USE COMPLETE PROMPT

**Copy this entire prompt:**

```
Create a comprehensive UML Class Diagram for the University of Ibadan ID Card Collection Status Tracker system using standard UML 2.0 notation.

CLASSES:

1. Student
   Stereotype: <<Model>>
   Attributes:
   - id: Integer {Primary Key}
   - matric_number: String {Unique, Not Null, Indexed}
   - name: String {Not Null}
   - department: String {Not Null}
   - status: String {Not Null, Default = 'Not Yet Printed'}
   - date_created: DateTime {Default = datetime.utcnow}
   - date_updated: DateTime {Default = datetime.utcnow, OnUpdate}
   
   Methods:
   + __repr__(): String
   + to_dict(): Dictionary

2. Admin
   Stereotype: <<Model>>
   Attributes:
   - id: Integer {Primary Key}
   - username: String {Unique, Not Null}
   - password: String {Not Null, Hashed}
   - email: String {Unique, Nullable}
   - full_name: String {Nullable}
   - date_created: DateTime {Default = datetime.utcnow}
   - last_login: DateTime {Nullable}
   
   Methods:
   + __repr__(): String
   + set_password(password: String): void
   + check_password(password: String): Boolean

3. FlaskApp
   Stereotype: <<Controller>>
   Attributes:
   - config: Dictionary
   - secret_key: String
   
   Methods:
   + route(path: String, methods: List): Decorator
   + run(host: String, port: Integer, debug: Boolean): void
   + index(): Response
   + search(): Response
   + admin_login(): Response
   + admin_dashboard(): Response
   + admin_upload(): Response
   + update_status(): JSON
   + admin_logout(): Response
   + allowed_file(filename: String): Boolean

4. SQLAlchemy (Database)
   Stereotype: <<Database>>
   Attributes:
   - session: Session
   
   Methods:
   + init_app(app: FlaskApp): void
   + create_all(): void
   + session.commit(): void
   + session.rollback(): void
   + query: Query

5. LoginManager
   Stereotype: <<Security>>
   Attributes:
   - login_view: String
   
   Methods:
   + init_app(app: FlaskApp): void
   + user_loader(callback: Function): void
   + login_user(user: Admin): void
   + logout_user(): void
   + login_required(): Decorator

6. UserMixin
   Stereotype: <<Interface>>
   Methods:
   + is_authenticated: Boolean
   + is_active: Boolean
   + is_anonymous: Boolean
   + get_id(): String

RELATIONSHIPS:

Inheritance:
- Student inherits from db.Model
- Admin inherits from db.Model
- Admin implements UserMixin

Composition:
- FlaskApp contains Database (composition)
- FlaskApp contains LoginManager (composition)

Dependency:
- FlaskApp uses Student
- FlaskApp uses Admin
- LoginManager uses Admin

Association:
- Database stores Student (1..*)
- Database stores Admin (1..*)

DIAGRAM SPECIFICATIONS:
- Use standard UML Class Diagram notation
- Classes as rectangles with three compartments: Name, Attributes, Methods
- Visibility: + (public), - (private), # (protected)
- Show data types and return types
- Inheritance: Solid line with hollow triangle arrow
- Implementation: Dashed line with hollow triangle arrow
- Composition: Solid line with filled diamond
- Dependency: Dashed arrow
- Association: Solid line with multiplicities
- Add stereotypes: <<Model>>, <<Controller>>, <<Database>>, <<Security>>, <<Interface>>
- Clear, readable labels
- Professional layout suitable for academic documentation

Generate a complete, professional Class Diagram following UML 2.0 standards.
```

---

## HOW TO USE

### In Miro AI:
1. Open Miro board
2. Click AI icon or press `/` and type "AI"
3. Select "Generate diagram" or "Create with AI"
4. Paste the complete prompt above
5. Click Generate
6. Customize classes, attributes, methods, and relationships as needed

### In Other Tools:
- **Draw.io**: Use prompt to get description, then create manually
- **Lucidchart**: Use AI feature with the prompt
- **PlantUML**: Ask AI to convert to PlantUML code first
- **Visual Paradigm**: Use the prompt in their AI assistant

---

## FOLLOW-UP PROMPTS

After generating, refine with:

- "Add multiplicities to all associations (1..*, 0..1, etc.)"
- "Show all method parameters with their types"
- "Add constraints in curly braces for attributes"
- "Make inheritance relationships more prominent"
- "Add notes explaining key relationships"
- "Create separate diagrams for Model classes and Controller classes"
- "Add return types to all methods"

---

## TIPS FOR BEST RESULTS

1. **Be Specific**: Use the detailed prompt for better results
2. **Iterate**: Generate, review, and ask for refinements
3. **Layout**: Request specific positioning (Models on left, Controllers in center, Database on right)
4. **Relationships**: Ensure all relationships are clearly shown with proper notation
5. **Details**: Include all attributes and methods for completeness
6. **Stereotypes**: Use stereotypes to categorize classes clearly

---

**This prompt is optimized for Miro AI, Draw.io, Lucidchart, PlantUML, and other UML diagramming tools!**

