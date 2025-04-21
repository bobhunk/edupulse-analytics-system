from abc import ABC, abstractmethod

class Assessment(ABC):
    """
    Abstract base class representing an assessment in the educational system.
    This class follows the OOP principle of abstraction.
    """
    
    @abstractmethod 
    def __init__(self, assessment_id, name, course_id, max_points):
        """
        Initialize an Assessment object.
        
        Args:
            assessment_id: Unique identifier for the assessment
            name: Name of the assessment
            course_id: ID of the course this assessment belongs to
            max_points: Maximum points possible for this assessment
        """
        self.assessment_id = assessment_id
        self.name = name
        self.course_id = course_id
        self.max_points = max_points
        self.grades = {}  # Dictionary mapping student IDs to scores
    
    def add_grade(self, student_id, score):
        """
        Add a grade for a student.
        
        Args:
            student_id: ID of the student
            score: Score achieved by the student
        """
        self.grades[student_id] = score
    
    def get_grade(self, student_id):
        """
        Get the grade for a specific student.
        
        Args:
            student_id: ID of the student
        
        Returns:
            The score for the student, or None if not found
        """
        return self.grades.get(student_id)
    
    def get_average_grade(self):
        """
        Calculate the average grade across all students.
        
        Returns:
            The average grade, or 0 if no grades exist
        """
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)
    
    def get_passing_rate(self, passing_score=60):
        """
        Calculate the percentage of students who passed the assessment.
        
        Args:
            passing_score: Minimum score required to pass (as a percentage)
        
        Returns:
            Percentage of students who passed, or 0 if no grades exist
        """
        if not self.grades:
            return 0
        
        passing_threshold = self.max_points * (passing_score / 100)
        passing_count = sum(1 for score in self.grades.values() if score >= passing_threshold)
        
        return (passing_count / len(self.grades)) * 100
    
    @abstractmethod
    def get_assessment_type(self):
        """Get the type of assessment."""
        pass
    
    def __str__(self):
        """String representation of the assessment."""
        return f"{self.name} ({self.get_assessment_type()}, {self.max_points} points)"


class Quiz(Assessment):
    """
    Class representing a quiz assessment.
    Inherits from Assessment class, demonstrating inheritance.
    """
    
    def __init__(self, assessment_id, name, course_id, max_points):
        """
        Initialize a Quiz object.
        
        Args:
            assessment_id: Unique identifier for the quiz
            name: Name of the quiz
            course_id: ID of the course this quiz belongs to
            max_points: Maximum points possible for this quiz
        """
        super().__init__(assessment_id, name, course_id, max_points)
    
    def get_assessment_type(self): # Quiz overrides the abstract method from Assessment class
        """Get the type of assessment."""
        return "Quiz"


class Exam(Assessment):
    """
    Class representing an exam assessment.
    Inherits from Assessment class, demonstrating inheritance.
    """
    
    def __init__(self, assessment_id, name, course_id, max_points):
        """
        Initialize an Exam object.
        
        Args:
            assessment_id: Unique identifier for the exam
            name: Name of the exam
            course_id: ID of the course this exam belongs to
            max_points: Maximum points possible for this exam
        """
        super().__init__(assessment_id, name, course_id, max_points)
    
    def get_assessment_type(self): # Exam overrides the abstract method from Assessment class
        """Get the type of assessment."""
        return "Exam"


class Project(Assessment):
    """
    Class representing a project assessment.
    Inherits from Assessment class, demonstrating inheritance.
    """
    
    def __init__(self, assessment_id, name, course_id, max_points):
        """
        Initialize a Project object.
        
        Args:
            assessment_id: Unique identifier for the project
            name: Name of the project
            course_id: ID of the course this project belongs to
            max_points: Maximum points possible for this project
        """
        super().__init__(assessment_id, name, course_id, max_points)
    
    def get_assessment_type(self):
        """Get the type of assessment."""
        return "Project"