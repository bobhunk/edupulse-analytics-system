"""
EduPulse: Educational Analytics Dashboard
Student Class Module

This module defines the Student class, which inherits from Person.
"""

# This Student class extends the Person base class and adds student-specific attributes and methods. It demonstrates inheritance, one of the key OOP principles.

from typing import Dict, Any, Optional, List
import json
from datetime import datetime
from models.person import Person

class Student(Person):
    """
    Class representing a student in the educational system.
    
    This class inherits from Person, demonstrating the OOP principle of inheritance.
    """
    
    def __init__(self, id: Optional[int], name: str, email: str, 
                enrollment_date: str, program: str, metadata: Dict = None):
        """
        Initialize a Student object.
        
        Args:
            id: Unique identifier (None for new students)
            name: Full name of the student
            email: Email address
            enrollment_date: Date of enrollment
            program: Academic program
            metadata: Additional student data
        """
        super().__init__(id, name, email)
        self._enrollment_date = enrollment_date
        self._program = program
        self._metadata = metadata or {}
    
    @property
    def enrollment_date(self) -> str:
        """Get the student's enrollment date."""
        return self._enrollment_date
    
    @enrollment_date.setter
    def enrollment_date(self, value: str) -> None:
        """Set the student's enrollment date."""
        self._enrollment_date = value
    
    @property
    def program(self) -> str:
        """Get the student's academic program."""
        return self._program
    
    @program.setter
    def program(self, value: str) -> None:
        """Set the student's academic program."""
        self._program = value
    
    @property
    def metadata(self) -> Dict:
        """Get the student's metadata."""
        return self._metadata
    
    @metadata.setter
    def metadata(self, value: Dict) -> None:
        """Set the student's metadata."""
        self._metadata = value
    
    def add_metadata(self, key: str, value: Any) -> None:
        """
        Add or update a metadata field.
        
        Args:
            key: Metadata key
            value: Metadata value
        """
        self._metadata[key] = value
    
    def get_metadata(self, key: str, default: Any = None) -> Any:
        """
        Get a metadata value by key.
        
        Args:
            key: Metadata key
            default: Default value if key not found
            
        Returns:
            Metadata value or default
        """
        return self._metadata.get(key, default)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the student object to a dictionary.
        
        Returns:
            Dictionary representation of the student
        """
        return {
            'id': self._id,
            'name': self._name,
            'email': self._email,
            'enrollment_date': self._enrollment_date,
            'program': self._program,
            'metadata': self._metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Student':
        """
        Create a student object from a dictionary.
        
        Args:
            data: Dictionary containing student data
            
        Returns:
            Student object
        """
        metadata = data.get('metadata')
        if isinstance(metadata, str):
            metadata = json.loads(metadata)
        
        return cls(
            id=data.get('id'),
            name=data['name'],
            email=data['email'],
            enrollment_date=data['enrollment_date'],
            program=data['program'],
            metadata=metadata
        )
    
    def calculate_enrollment_duration(self) -> int:
        """
        Calculate the duration since enrollment in days.
        
        Returns:
            Number of days since enrollment
        """
        enrollment = datetime.strptime(self._enrollment_date, '%Y-%m-%d')
        today = datetime.now()
        return (today - enrollment).days
    
    def __str__(self) -> str:
        """String representation of the student."""
        return f"Student(id={self._id}, name={self._name}, program={self._program})"