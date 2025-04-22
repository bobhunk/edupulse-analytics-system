"""
EduPulse: Educational Analytics Dashboard
Abstract Analyzer Class

This module defines the base analyzer class for data analysis.
"""
# This abstract Analyzer class defines the interface that all analyzer classes must implement. It demonstrates the OOP principle of abstraction,
# by defining abstract methods that subclasses must implement.

from abc import ABC, abstractmethod
from typing import Dict, Any, List
from database.db_manager import DatabaseManager

class Analyzer(ABC):
    """
    Abstract base class for data analyzers.
    
    This class demonstrates the OOP principle of abstraction.
    """
    
    def __init__(self, db_manager: DatabaseManager):
        """
        Initialize the analyzer with a database manager.
        
        Args:
            db_manager: Database manager for data access
        """
        self.db_manager = db_manager
    
    @abstractmethod
    def analyze(self, data_id: int) -> Dict[str, Any]: # hides the implementation details of the analysis process
        """
        Analyze data for a specific entity.
        
        Args:
            data_id: ID of the entity to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        pass
    
    @abstractmethod
    def get_analyzer_type(self) -> str:
        """
        Get the type of analyzer.
        
        Returns:
            Analyzer type string
        """
        pass