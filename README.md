# EduPulse: Educational Analytics Dashboard

## Project Overview
EduPulse is an educational analytics dashboard designed to help higher education institutions effectively utilize student data for improving performance and retention. This project demonstrates object-oriented programming principles in Python, focusing on student performance tracking and early warning systems.

## Features
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
│   │   └── style.css
│   └── js/
│       └── main.js
├── templates/
│   ├── analytics.html
│   ├── base.html
│   ├── courses.html
│   ├── dashboard.html
│   └── students.html
├── routes/
│   ├── __init__.py
│   └── analytics.py
├── app.py
├── db_manager.py
└── README.md
```

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

## Usage

### Admin Dashboard
- View overall system statistics
- Manage courses and enrollments
- Generate reports

### Lecturer View
- Monitor course performance
- Track attendance
- Identify at-risk students
- Record assessment results

### Student View
- View personal performance metrics
- Check attendance records
- Access course materials

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Authors
- Robert Tumushiime - MSc Data Science Student, UCU

## Acknowledgments
- Uganda Christian University
- Faculty of Science and Technology
- Object Oriented Programming Course Instructors