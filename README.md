# EduPulse: Educational Analytics Dashboard

## Project Overview
EduPulse is an educational analytics dashboard designed to help higher education institutions effectively utilize student data for improving performance and retention. This project demonstrates object-oriented programming principles in Python, focusing on student performance tracking and early warning systems.

## Features

## Role Based Dashboards

## Student Dashboard

- View grades and performance trends
- Check attendance patterns
- View enrolled courses
- Message lecturers for queries
- Track personal academic progress

## Lecturer Dashboard

- Track class performance metrics
- Upload student marks
- Generate student reports
- Identify students needing support
- View course-related analytics
- Message students for course queries
- Administrator Dashboard
- View institution-wide analytics
- Add new students to the system
- Add new lecturers to the system
- Manage system settings
- Generate institutional reports

# Technical Features

- **Data Integration & Management**
  - Import and manage student records
  - Track course enrollments
  - Record attendance and assessment results
  - Handle multiple assessment types (quizzes, exams, projects)

- **Analysis Engine**
  - Monitor student performance metrics
  - Calculate weighted averages across assessments
  - Track attendance patterns
  - Identify at-risk students based on configurable thresholds
  - Generate performance reports

- **User Interface**
  - Role-based access control (students, lecturers, administrators)
  - Responsive Bootstrap-based design
  - Interactive data tables
  - Performance summary cards
  - Early warning indicators

## Technology Stack
- **Backend**
  - Python 3.9+
  - Flask web framework
  - SQLite database
  - Pandas for data processing
  
- **Frontend**
  - Bootstrap 5 for responsive design
  - Font Awesome icons
  - Custom CSS

## Project Structure
```
EduPulse/
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── dashboard.css
│   └── js/
│       └── main.js
├── templates/
│   ├── main_dashboard.html
│   ├── student_dashboard.html
│   ├── lecturer_dashboard.html
│   ├── admin_dashboard.html
│   ├── base.html
│   ├── courses.html
│   ├── analytics.html
│   ├── reports.html
|
├── routes/
│   ├── __init__.py
│   ├── analytics.py
│   ├── auth.py
│   └── dashboard.py
├── models/
│   ├── __init__.py
│   ├── student.py
│   ├── lecturer.py
│   └── course.py
├── app.py
├── db_manager.py
├── requirements.txt
└── README.md

## Key Components

### Database Schema
- **Students**: Personal and academic information
- **Courses**: Course details and metadata
- **Enrollments**: Student-course relationships
- **Assessments**: Different types of evaluations
- **Assessment Results**: Student performance records
- **Attendance**: Class attendance tracking

### Core Classes
- **DatabaseManager**: Handles all database operations
- **Student**: Student entity management
- **Course**: Course information and enrollment
- **Assessment**: Base class for various assessment types
  - Quiz
  - Exam
  - Project

## Setup and Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd edupulse
```

2. Create a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
python app.py
```

5. Access the application:
```
http://localhost:5000
```


## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Authors
- Bob Robert Tumushiime - MSc Data Science Student, Uganda Christian University

## Acknowledgments
- Uganda Christian University
- Faculty of Science and Technology