"""
EduPulse: Educational Analytics Dashboard
lecturer Class Module

This module defines the lecturer class, which inherits from Person.
"""
# This lecturer class also extends the Person base class and adds lecturer-specific attributes and methods. Like the Student class, it demonstrates inheritance from the abstract base class.

from typing import Dict, Any, Optional, List
import json
from models.person import Person

class lecturer(Person):
    """
    Class representing an lecturer in the educational system.
    
    This class inherits from Person, demonstrating the OOP principle of inheritance.
    """
    
    def __init__(self, id: Optional[int], name: str, email: str, 
                department: str, metadata: Dict = None):
        """
        Initialize an lecturer object.
        
        Args:
            id: Unique identifier (None for new lecturers)
            name: Full name of the lecturer
            email: Email address
            department: Academic department
            metadata: Additional lecturer data
        """
        super().__init__(id, name, email)
        self._department = department
        self._metadata = metadata or {}
    
    @property
    def department(self) -> str:
        """Get the lecturer's department."""
        return self._department
    
    @department.setter
    def department(self, value: str) -> None:
        """Set the lecturer's department."""
        self._department = value
    
    @property
    def metadata(self) -> Dict:
        """Get the lecturer's metadata."""
        return self._metadata
    
    @metadata.setter
    def metadata(self, value: Dict) -> None:
        """Set the lecturer's metadata."""
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
        Convert the lecturer object to a dictionary.
        
        Returns:
            Dictionary representation of the lecturer
        """
        return {
            'id': self._id,
            'name': self._name,
            'email': self._email,
            'department': self._department,
            'metadata': self._metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'lecturer':
        """
        Create an lecturer object from a dictionary.
        
        Args:
            data: Dictionary containing lecturer data
            
        Returns:
            lecturer object
        """
        metadata = data.get('metadata')
        if isinstance(metadata, str):
            metadata = json.loads(metadata)
        
        return cls(
            id=data.get('id'),
            name=data['name'],
            email=data['email'],
            department=data['department'],
            metadata=metadata
        )
    
    def __str__(self) -> str:
        """String representation of the lecturer."""
        return f"lecturer(id={self._id}, name={self._name}, department={self._department})"