from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'

# Simple authentication context
class SimpleUser:
    def __init__(self, is_authenticated=False):
        self.is_authenticated = is_authenticated

@app.context_processor
def inject_user():
    return dict(current_user=SimpleUser(is_authenticated=session.get('admin_logged_in', False)))

# Simple in-memory storage for demo
students = [
    {
        'id': 1,
        'matric_number': '222486',
        'name': 'John Doe',
        'department': 'Computer Science',
        'status': 'Available',
        'date_created': datetime.utcnow(),
        'date_updated': datetime.utcnow()
    },
    {
        'id': 2,
        'matric_number': '222736',
        'name': 'Jane Smith',
        'department': 'Mathematics',
        'status': 'Collected',
        'date_created': datetime.utcnow(),
        'date_updated': datetime.utcnow()
    },
    {
        'id': 3,
        'matric_number': '222845',
        'name': 'Michael Johnson',
        'department': 'Physics',
        'status': 'Available',
        'date_created': datetime.utcnow(),
        'date_updated': datetime.utcnow()
    },
    {
        'id': 4,
        'matric_number': '222934',
        'name': 'Sarah Wilson',
        'department': 'Chemistry',
        'status': 'Processing',
        'date_created': datetime.utcnow(),
        'date_updated': datetime.utcnow()
    },
    {
        'id': 5,
        'matric_number': '223127',
        'name': 'David Brown',
        'department': 'Biology',
        'status': 'Available',
        'date_created': datetime.utcnow(),
        'date_updated': datetime.utcnow()
    }
]

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        matric_number = request.form.get('matric_number', '').strip().upper()
        if matric_number:
            student = next((s for s in students if s['matric_number'] == matric_number), None)
            if student:
                return render_template('search_result.html', student=student)
            else:
                flash('Student not found. Please check your matric number.', 'error')
        else:
            flash('Please enter a matric number.', 'error')
    return render_template('search.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == 'admin123':
            session['admin_logged_in'] = True
            flash('Login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        flash('Please log in to access the admin dashboard.', 'error')
        return redirect(url_for('admin_login'))
    return render_template('admin_dashboard.html', students=students)

@app.route('/admin/upload', methods=['GET', 'POST'])
def admin_upload():
    if not session.get('admin_logged_in'):
        flash('Please log in to access the admin upload.', 'error')
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        flash('File upload feature requires database setup. Please install required packages.', 'info')
    return render_template('admin_upload.html')

@app.route('/admin/update_status', methods=['POST'])
def update_status():
    if not session.get('admin_logged_in'):
        return jsonify({'success': False, 'message': 'Authentication required'}), 401
    
    data = request.get_json()
    student_id = data.get('student_id')
    new_status = data.get('status')
    
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        student['status'] = new_status
        student['date_updated'] = datetime.utcnow()
        return jsonify({'success': True, 'message': 'Status updated successfully'})
    
    return jsonify({'success': False, 'message': 'Student not found'}), 404

if __name__ == '__main__':
    print("Starting ID Card Tracker Server...")
    print("Access the application at: http://localhost:5000")
    print("Admin login: username='admin', password='admin123'")
    app.run(debug=True, host='0.0.0.0', port=5000)
