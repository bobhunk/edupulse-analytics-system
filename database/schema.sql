-- EduPulse Database Schema

-- Students table
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    enrollment_date TEXT NOT NULL,
    program TEXT NOT NULL,
    metadata TEXT
);

-- lecturers table
CREATE TABLE IF NOT EXISTS lecturers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    department TEXT NOT NULL,
    metadata TEXT
);

-- Courses table
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    lecturer_id INTEGER NOT NULL,
    semester TEXT NOT NULL,
    year INTEGER NOT NULL,
    FOREIGN KEY (lecturer_id) REFERENCES lecturers (id)
);

-- Student-Course enrollments
CREATE TABLE IF NOT EXISTS enrollments (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrollment_date TEXT NOT NULL,
    status TEXT NOT NULL,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (course_id) REFERENCES courses (id)
);

-- Assessments table
CREATE TABLE IF NOT EXISTS assessments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    type TEXT NOT NULL,
    max_score REAL NOT NULL,
    weight REAL NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses (id)
);

-- Student assessment scores
CREATE TABLE IF NOT EXISTS scores (
    student_id INTEGER NOT NULL,
    assessment_id INTEGER NOT NULL,
    score REAL NOT NULL,
    submission_date TEXT,
    feedback TEXT,
    PRIMARY KEY (student_id, assessment_id),
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (assessment_id) REFERENCES assessments (id)
);

-- Attendance records
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (course_id) REFERENCES courses (id)
);