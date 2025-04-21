"""
EduPulse: Educational Analytics Dashboard
Database Manager Module

This module handles all database operations including connections,
queries, and data manipulation.
"""

import os
import sqlite3
from datetime import datetime

class DatabaseManager:
    """
    Database manager for the EduPulse application.
    Handles all database operations including connecting to the database,
    setting up the schema, and providing methods to add and retrieve data.
    """
    
    def __init__(self, db_path):
        """
        Initialize the database manager with the path to the database file.
        
        Args:
            db_path (str): Path to the SQLite database file
        """
        self.db_path = db_path
        self.conn = None
        self.setup_database()
    
    def connect(self):
        """
        Connect to the SQLite database.
        
        Returns:
            sqlite3.Connection: Database connection
        """
        # Ensure directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        # Connect to database with row factory to get dict-like results
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def setup_database(self):
        """
        Set up the database schema if it doesn't exist.
        """
        # Create tables based on schema
        conn = self.connect()
        cursor = conn.cursor()
        
        # Students table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            enrollment_date TEXT,
            department TEXT
        )
        ''')
        
        # lecturers table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            department TEXT
        )
        ''')
        
        # Courses table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_code TEXT UNIQUE NOT NULL,
            title TEXT NOT NULL,
            lecturer_id INTEGER,
            semester TEXT,
            year INTEGER,
            FOREIGN KEY (lecturer_id) REFERENCES lecturers (id)
        )
        ''')
        
        # Enrollments table (many-to-many relationship between students and courses)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            student_id INTEGER,
            course_id INTEGER,
            enrollment_date TEXT,
            status TEXT,
            PRIMARY KEY (student_id, course_id),
            FOREIGN KEY (student_id) REFERENCES students (id),
            FOREIGN KEY (course_id) REFERENCES courses (id)
        )
        ''')
        
        # Assessments table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            max_points INTEGER,
            weight REAL,
            due_date TEXT,
            FOREIGN KEY (course_id) REFERENCES courses (id)
        )
        ''')
        
        # Scores table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            student_id INTEGER,
            assessment_id INTEGER,
            score REAL,
            submission_date TEXT,
            PRIMARY KEY (student_id, assessment_id),
            FOREIGN KEY (student_id) REFERENCES students (id),
            FOREIGN KEY (assessment_id) REFERENCES assessments (id)
        )
        ''')
        
        # Attendance table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            student_id INTEGER,
            course_id INTEGER,
            date TEXT,
            status TEXT,
            PRIMARY KEY (student_id, course_id, date),
            FOREIGN KEY (student_id) REFERENCES students (id),
            FOREIGN KEY (course_id) REFERENCES courses (id)
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def is_empty(self):
        """
        Check if the database is empty.
        
        Returns:
            bool: True if the database is empty, False otherwise
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        # Check if students table is empty
        cursor.execute("SELECT COUNT(*) FROM students")
        student_count = cursor.fetchone()[0]
        
        conn.close()
        return student_count == 0
    
    def execute_query(self, query, params=()):
        """
        Execute a SQL query and return the results.
        
        Args:
            query (str): SQL query to execute
            params (tuple): Parameters for the query
            
        Returns:
            list: List of rows returned by the query
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute(query, params)
        
        # If the query is a SELECT query, return the results
        if query.strip().upper().startswith("SELECT"):
            results = cursor.fetchall()
            conn.close()
            return results
        
        # Otherwise, commit the changes and return None
        conn.commit()
        conn.close()
        return None
    
    # Student methods
    def add_student(self, name, email, enrollment_date, department):
        """
        Add a new student to the database.
        
        Args:
            name (str): Student's full name
            email (str): Student's email
            enrollment_date (str): Date of enrollment (YYYY-MM-DD)
            department (str): Student's department
            
        Returns:
            int: ID of the new student
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO students (name, email, enrollment_date, department) VALUES (?, ?, ?, ?)",
            (name, email, enrollment_date, department)
        )
        
        student_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return student_id
    
    def get_student(self, student_id):
        """
        Get a student by ID.
        
        Args:
            student_id (int): Student ID
            
        Returns:
            dict: Student data
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student = cursor.fetchone()
        
        conn.close()
        return dict(student) if student else None
    
    # lecturer methods
    def add_lecturer(self, name, email, department):
        """
        Add a new lecturer to the database.
        
        Args:
            name (str): lecturer's full name
            email (str): lecturer's email
            department (str): lecturer's department
            
        Returns:
            int: ID of the new lecturer
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO lecturers (name, email, department) VALUES (?, ?, ?)",
            (name, email, department)
        )
        
        lecturer_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return lecturer_id
    
    def get_lecturer(self, lecturer_id):
        """
        Get an lecturer by ID.
        
        Args:
            lecturer_id (int): lecturer ID
            
        Returns:
            dict: lecturer data
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM lecturers WHERE id = ?", (lecturer_id,))
        lecturer = cursor.fetchone()
        
        conn.close()
        return dict(lecturer) if lecturer else None
    
    def get_lecturer_courses(self, lecturer_id):
        """
        Get all courses taught by an lecturer.
        
        Args:
            lecturer_id (int): lecturer ID
            
        Returns:
            list: List of courses
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM courses WHERE lecturer_id = ?", (lecturer_id,))
        courses = cursor.fetchall()
        
        conn.close()
        return [dict(course) for course in courses]
    
    # Course methods
    def add_course(self, course_code, title, lecturer_id, semester, year):
        """
        Add a new course to the database.
        
        Args:
            course_code (str): Course code
            title (str): Course title
            lecturer_id (int): ID of the lecturer teaching the course
            semester (str): Semester
            year (int): Year
            
        Returns:
            int: ID of the new course
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO courses (course_code, title, lecturer_id, semester, year) VALUES (?, ?, ?, ?, ?)",
            (course_code, title, lecturer_id, semester, year)
        )
        
        course_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return course_id
    
    def get_course(self, course_id):
        """
        Get a course by ID.
        
        Args:
            course_id (int): Course ID
            
        Returns:
            dict: Course data
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM courses WHERE id = ?", (course_id,))
        course = cursor.fetchone()
        
        conn.close()
        return dict(course) if course else None
    
    # Assessment methods
    def add_assessment(self, course_id, name, assessment_type, max_points, weight, due_date):
        """
        Add a new assessment to the database.
        
        Args:
            course_id (int): ID of the course
            name (str): Assessment name
            assessment_type (str): Type of assessment (Quiz, Exam, Project)
            max_points (int): Maximum points
            weight (float): Weight of the assessment in the final grade
            due_date (str): Due date (YYYY-MM-DD)
            
        Returns:
            int: ID of the new assessment
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO assessments (course_id, name, type, max_points, weight, due_date) VALUES (?, ?, ?, ?, ?, ?)",
            (course_id, name, assessment_type, max_points, weight, due_date)
        )
        
        assessment_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return assessment_id
    
    def get_course_assessments(self, course_id):
        """
        Get all assessments for a course.
        
        Args:
            course_id (int): Course ID
            
        Returns:
            list: List of assessments
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM assessments WHERE course_id = ?", (course_id,))
        assessments = cursor.fetchall()
        
        conn.close()
        return [dict(assessment) for assessment in assessments]
    
    # Score methods
    def add_score(self, student_id, assessment_id, score, submission_date=None):
        """
        Add a score for a student's assessment.
        
        Args:
            student_id (int): Student ID
            assessment_id (int): Assessment ID
            score (float): Score
            submission_date (str, optional): Submission date (YYYY-MM-DD)
            
        Returns:
            bool: True if successful
        """
        if submission_date is None:
            submission_date = datetime.now().strftime("%Y-%m-%d")
            
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT OR REPLACE INTO scores (student_id, assessment_id, score, submission_date) VALUES (?, ?, ?, ?)",
            (student_id, assessment_id, score, submission_date)
        )
        
        conn.commit()
        conn.close()
        
        return True
    
    def get_student_scores(self, student_id, course_id=None):
        """
        Get all scores for a student, optionally filtered by course.
        
        Args:
            student_id (int): Student ID
            course_id (int, optional): Course ID
            
        Returns:
            list: List of scores
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        if course_id:
            cursor.execute("""
                SELECT s.*, a.name as assessment_name, a.type as assessment_type, a.max_points, a.weight
                FROM scores s
                JOIN assessments a ON s.assessment_id = a.id
                WHERE s.student_id = ? AND a.course_id = ?
            """, (student_id, course_id))
        else:
            cursor.execute("""
                SELECT s.*, a.name as assessment_name, a.type as assessment_type, a.max_points, a.weight
                FROM scores s
                JOIN assessments a ON s.assessment_id = a.id
                WHERE s.student_id = ?
            """, (student_id,))
            
        scores = cursor.fetchall()
        
        conn.close()
        return [dict(score) for score in scores]
    
    # Attendance methods
    def add_attendance(self, student_id, course_id, date, status):
        """
        Add an attendance record.
        
        Args:
            student_id (int): Student ID
            course_id (int): Course ID
            date (str): Date (YYYY-MM-DD)
            status (str): Attendance status (present, late, absent)
            
        Returns:
            bool: True if successful
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT OR REPLACE INTO attendance (student_id, course_id, date, status) VALUES (?, ?, ?, ?)",
            (student_id, course_id, date, status)
        )
        
        conn.commit()
        conn.close()
        
        return True
    
    def get_student_attendance(self, student_id, course_id):
        """
        Get attendance records for a student in a course.
        
        Args:
            student_id (int): Student ID
            course_id (int): Course ID
            
        Returns:
            list: List of attendance records
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM attendance
            WHERE student_id = ? AND course_id = ?
            ORDER BY date
        """, (student_id, course_id))
        
        attendance = cursor.fetchall()
        
        conn.close()
        return [dict(record) for record in attendance]