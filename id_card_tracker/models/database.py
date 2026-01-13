from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class Student(db.Model):
    """Student model for storing student information and ID card status"""
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    matric_number = db.Column(db.String(20), unique=True, nullable=False, index=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Not Yet Printed')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Student {self.matric_number}: {self.name}>'
    
    def to_dict(self):
        """Convert student object to dictionary for JSON responses"""
        return {
            'id': self.id,
            'matric_number': self.matric_number,
            'name': self.name,
            'department': self.department,
            'status': self.status,
            'date_created': self.date_created.isoformat() if self.date_created else None,
            'date_updated': self.date_updated.isoformat() if self.date_updated else None
        }

class Admin(UserMixin, db.Model):
    """Admin model for ITEMS staff authentication"""
    __tablename__ = 'admins'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    full_name = db.Column(db.String(100), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return f'<Admin {self.username}>'
    
    def set_password(self, password):
        """Hash and set password"""
        from werkzeug.security import generate_password_hash
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if provided password matches"""
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password) 