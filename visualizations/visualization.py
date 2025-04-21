"""
EduPulse: Educational Analytics Dashboard
Abstract Visualization Class

This module defines the base visualization class.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List

class Visualization(ABC):
    """
    Abstract base class for data visualizations.
    
    This class demonstrates the OOP principle of abstraction.
    """
    
    @abstractmethod
    def generate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate visualization data.
        
        Args:
            data: Data to visualize
            
        Returns:
            Dictionary containing visualization configuration
        """
        pass
    
    @abstractmethod
    def get_visualization_type(self) -> str:
        """
        Get the type of visualization.
        
        Returns:
            Visualization type string
        """
        pass