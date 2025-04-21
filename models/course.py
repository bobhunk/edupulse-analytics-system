class Course:
    """
    Class representing a course in the educational system.
    Demonstrates encapsulation by managing its own data and providing controlled access.
    """
    
    def __init__(self, course_id, course_name, lecturer_id, course_code):
        """
        Initialize a Course object.
        
        Args:
            course_id: Unique identifier for the course
            course_name: Name of the course
            lecturer_id: ID of the lecturer teaching the course
            course_code: Course code (e.g., CS101)
        """
        self.course_id = course_id
        self.course_name = course_name
        self.lecturer_id = lecturer_id
        self.course_code = course_code
        self.students = []  # List of students enrolled in the course
        self.assessments = []  # List of assessments for the course
    
    def add_student(self, student):
        """
        Add a student to the course.
        
        Args:
            student: Student object to add
        """
        if student not in self.students:
            self.students.append(student)
            student.enroll_in_course(self)
    
    def add_students(self, students):
        """
        Add multiple students to the course.
        
        Args:
            students: List of Student objects to add
        """
        for student in students:
            self.add_student(student)
    
    def remove_student(self, student):
        """
        Remove a student from the course.
        
        Args:
            student: Student object to remove
        """
        if student in self.students:
            self.students.remove(student)
    
    def add_assessment(self, assessment):
        """
        Add an assessment to the course.
        
        Args:
            assessment: Assessment object to add
        """
        if assessment not in self.assessments:
            self.assessments.append(assessment)
    
    def get_student_count(self):
        """
        Get the number of students enrolled in the course.
        
        Returns:
            Number of students
        """
        return len(self.students)
    
    def get_average_grade(self):
        """
        Calculate the average grade across all students and assessments.
        
        Returns:
            The average grade, or 0 if no grades exist
        """
        if not self.students or not self.assessments:
            return 0
        
        total_score = 0
        total_count = 0
        
        for student in self.students:
            for assessment in self.assessments:
                grade = student.get_grade(assessment.assessment_id)
                if grade is not None:
                    total_score += grade
                    total_count += 1
        
        return total_score / total_count if total_count > 0 else 0
    
    def get_at_risk_students(self, threshold=60):
        """
        Identify students who are at risk based on their average grade.
        
        Args:
            threshold: Grade threshold below which students are considered at risk
        
        Returns:
            List of at-risk students
        """
        at_risk = []
        
        for student in self.students:
            avg_grade = 0
            grade_count = 0
            
            for assessment in self.assessments:
                grade = student.get_grade(assessment.assessment_id)
                if grade is not None:
                    avg_grade += grade / assessment.max_points * 100
                    grade_count += 1
            
            if grade_count > 0:
                avg_grade /= grade_count
                if avg_grade < threshold:
                    at_risk.append(student)
        
        return at_risk
    
    def __str__(self):
        """String representation of the course."""
        return f"{self.course_code}: {self.course_name} ({self.get_student_count()} students)"