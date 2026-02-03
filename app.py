from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-change-this-in-production')

# Database configuration - Using SQLite (file-based database)
# To use MySQL instead, set DB_TYPE=mysql in .env file
db_type = os.getenv('DB_TYPE', 'sqlite').lower()

if db_type == 'mysql':
    # MySQL configuration (optional - for production)
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = os.getenv('DB_PORT', '3306')
    db_user = os.getenv('DB_USER', 'tracker_user')
    db_password = os.getenv('DB_PASSWORD', '')
    db_name = os.getenv('DB_NAME', 'id_card_tracker')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    print(f"✅ Using MySQL database: {db_name} on {db_host}")
else:
    # SQLite - default database (no setup required!)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///id_cards.db'
    print("✅ Using SQLite database (no configuration needed)")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Import models first
from models.database import Student, Admin, db

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        matric_number = request.form.get('matric_number', '').strip().upper()
        
        # Clean and validate matric number (remove slashes, keep only digits)
        matric_number = ''.join(filter(str.isdigit, matric_number))
        
        if matric_number and len(matric_number) == 6:
            student = Student.query.filter_by(matric_number=matric_number).first()
            if student:
                return render_template('search_result.html', student=student)
            else:
                flash('Student not found. Please check your matric number.', 'error')
        elif matric_number:
            flash('Matric number must be exactly 6 digits.', 'error')
        else:
            flash('Please enter a matric number.', 'error')
    return render_template('search.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        admin = Admin.query.filter_by(username=username).first()
        if admin and check_password_hash(admin.password, password):
            login_user(admin)
            flash('Login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('admin_login.html')

@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    students = Student.query.order_by(Student.name).all()
    return render_template('admin_dashboard.html', students=students)

@app.route('/admin/upload', methods=['GET', 'POST'])
@login_required
def admin_upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected.', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected.', 'error')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            try:
                try:
                    import pandas as pd
                except Exception as e:
                    flash(f'Error loading data processing library (pandas): {str(e)}', 'error')
                    return redirect(request.url)
                
                # Read Excel/CSV file
                if file.filename.endswith('.csv'):
                    df = pd.read_csv(file)
                    print(f"✅ Reading CSV file: {file.filename}")
                elif file.filename.endswith(('.xlsx', '.xls')):
                    df = pd.read_excel(file)
                    print(f"✅ Reading Excel file: {file.filename}")
                else:
                    flash('Unsupported file format. Please use .csv, .xlsx, or .xls files.', 'error')
                    return redirect(request.url)
                
                # Process the data
                success_count = 0
                for _, row in df.iterrows():
                    matric_number = str(row['matric_number']).strip().upper()
                    # Clean matric number - remove slashes and non-digits, keep only 6 digits
                    matric_number = ''.join(filter(str.isdigit, matric_number))
                    name = str(row['name']).strip()
                    department = str(row['department']).strip()
                    status = str(row['status']).strip()
                    
                    # Validate matric number is 6 digits
                    if not matric_number or len(matric_number) != 6:
                        continue  # Skip invalid matric numbers
                    
                    # Check if student exists
                    student = Student.query.filter_by(matric_number=matric_number).first()
                    if student:
                        # Update existing student
                        student.name = name
                        student.department = department
                        student.status = status
                        student.date_updated = datetime.utcnow()
                    else:
                        # Create new student
                        new_student = Student(
                            matric_number=matric_number,
                            name=name,
                            department=department,
                            status=status
                        )
                        db.session.add(new_student)
                    
                    success_count += 1
                
                db.session.commit()
                flash(f'Successfully processed {success_count} students.', 'success')
                return redirect(url_for('admin_dashboard'))
                
            except Exception as e:
                flash(f'Error processing file: {str(e)}', 'error')
                db.session.rollback()
        else:
            flash('Invalid file type. Please upload .csv, .xlsx, or .xls files.', 'error')
    
    return render_template('admin_upload.html')

@app.route('/admin/update_status', methods=['POST'])
@login_required
def update_status():
    data = request.get_json()
    student_id = data.get('student_id')
    new_status = data.get('status')
    
    student = Student.query.get(student_id)
    if student:
        student.status = new_status
        student.date_updated = datetime.utcnow()
        db.session.commit()
        return jsonify({'success': True, 'message': 'Status updated successfully'})
    
    return jsonify({'success': False, 'message': 'Student not found'}), 404

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'csv', 'xlsx', 'xls'}

if __name__ == '__main__':
    with app.app_context():
        # Create all database tables
        db.create_all()
        
        # Create default admin user if none exists
        if not Admin.query.first():
            default_admin = Admin(
                username='admin',
                password=generate_password_hash('admin123')
            )
            db.session.add(default_admin)
            db.session.commit()
            print("Default admin user created: username='admin', password='admin123'")
    
    # Production settings
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(debug=debug, host='0.0.0.0', port=port) 