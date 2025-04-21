from typing import List, Dict, Any
from visualizations.line_chart import Visualization

class Dashboard:
    """
    Class representing a dashboard that orchestrates multiple visualizations.
    Demonstrates composition by containing visualization objects.
    """
    
    def __init__(self, title: str):
        """
        Initialize a Dashboard object.
        
        Args:
            title: Title of the dashboard
        """
        self.title = title
        self.visualizations = []
    
    def add_visualization(self, visualization: Visualization):
        """
        Add a visualization to the dashboard.
        
        Args:
            visualization: Visualization object to add
        """
        self.visualizations.append(visualization)
    
    def get_visualizations(self) -> List[Visualization]:
        """
        Get all visualizations in the dashboard.
        
        Returns:
            List of visualization objects
        """
        return self.visualizations
    
    def get_visualization_jsons(self) -> List[str]:
        """
        Get all visualizations as JSON strings for web display.
        
        Returns:
            List of JSON string representations of visualizations
        """
        return [viz.to_json() for viz in self.visualizations]
    
    def clear_visualizations(self):
        """Remove all visualizations from the dashboard."""
        self.visualizations = []
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get a summary of the dashboard.
        
        Returns:
            Dictionary with dashboard summary information
        """
        return {
            'title': self.title,
            'visualization_count': len(self.visualizations),
            'visualization_types': [viz.__class__.__name__ for viz in self.visualizations]
        }
    
    def __str__(self) -> str:
        """String representation of the dashboard."""
        return f"{self.title} Dashboard with {len(self.visualizations)} visualizations"