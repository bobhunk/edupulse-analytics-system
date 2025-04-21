from abc import ABC, abstractmethod

class Person(ABC):
    """
    Abstract base class representing a person in the educational system.
    This class follows the OOP principle of abstraction.
    """
    
    @abstractmethod
    def __init__(self, id, first_name, last_name, email, department):
        """
        Initialize a Person object.
        
        Args:
            id: Unique identifier for the person
            first_name: First name of the person
            last_name: Last name of the person
            email: Email address of the person
            department: Department the person belongs to
        """
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.department = department
    
    @property
    def full_name(self):
        """Get the full name of the person."""
        return f"{self.first_name} {self.last_name}"
    
    @abstractmethod
    def get_role(self):
        """Get the role of the person in the educational system."""
        pass
    
    def __str__(self):
        """String representation of the person."""
        return f"{self.full_name} ({self.get_role()})"


class Student(Person):
    """
    Class representing a student in the educational system.
    Inherits from Person class, demonstrating inheritance.
    """
    
    def __init__(self, student_id, first_name, last_name, email, department):
        """
        Initialize a Student object.
        
        Args:
            student_id: Unique identifier for the student
            first_name: First name of the student
            last_name: Last name of the student
            email: Email address of the student
            department: Department the student belongs to
        """
        super().__init__(student_id, first_name, last_name, email, department)
        self.student_id = student_id
        self.courses = []  # List of courses the student is enrolled in
        self.grades = {}   # Dictionary mapping assessment IDs to grades
    
    def get_role(self):
        """Get the role of the person in the educational system."""
        return "Student"
    
    def enroll_in_course(self, course):
        """
        Enroll the student in a course.
        
        Args:
            course: Course object to enroll in
        """
        if course not in self.courses:
            self.courses.append(course)
    
    def add_grade(self, assessment_id, score):
        """
        Add a grade for an assessment.
        
        Args:
            assessment_id: ID of the assessment
            score: Score achieved by the student
        """
        self.grades[assessment_id] = score
    
    def get_grade(self, assessment_id):
        """
        Get the grade for a specific assessment.
        
        Args:
            assessment_id: ID of the assessment
        
        Returns:
            The score for the assessment, or None if not found
        """
        return self.grades.get(assessment_id)
    
    def get_average_grade(self):
        """
        Calculate the average grade across all assessments.
        
        Returns:
            The average grade, or 0 if no grades exist
        """
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)


class lecturer(Person):
    """
    Class representing a lecturer in the educational system.
    Inherits from Person class, demonstrating inheritace.
    """
    
    def __init__(self, lecturer_id, first_name, last_name, email, department):
        """
        Initialize a lecturer object.
        
        Args:
            lecturer_id: Unique identifier for the lecturer
            first_name: First name of the lecturer
            last_name: Last name of the lecturer
            email: Email address of the lecturer
            department: Department the lecturer belongs to
        """
        super().__init__(lecturer_id, first_name, last_name, email, department)
        self.lecturer_id = lecturer_id
        self.courses = []  # List of courses the lecturer teaches
    
    def get_role(self):
        """Get the role of the person in the educational system."""
        return "lecturer"
    
    def assign_course(self, course):
        """
        Assign a course to the lecturer.
        
        Args:
            course: Course object to assign
        """
        if course not in self.courses:
            self.courses.append(course)
    
    def get_student_count(self):
        """
        Get the total number of students across all courses taught by the lecturer.
        
        Returns:
            Total number of students
        """
        # Use a set to avoid counting students multiple times
        students = set()
        for course in self.courses:
            for student in course.students:
                students.add(student.student_id)
        return len(students)
    
    def grade_assessment(self, student, assessment, score):
        """
        Grade a student's assessment.
        
        Args:
            student: Student object
            assessment: Assessment object
            score: Score to assign
        """
        student.add_grade(assessment.assessment_id, score)
        assessment.add_grade(student.student_id, score)