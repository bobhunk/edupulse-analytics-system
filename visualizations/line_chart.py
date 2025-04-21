from abc import ABC, abstractmethod
import plotly.graph_objects as go
import plotly.express as px
import json
from typing import Dict, List, Any

class Visualization(ABC):
    """
    Abstract base class for visualizations in the EduPulse system.
    This class follows the OOP principle of abstraction.
    """
    
    @abstractmethod
    def __init__(self, title: str, data: Dict[str, Any]):
        """
        Initialize a Visualization object.
        
        Args:
            title: Title of the visualization
            data: Data to visualize
        """
        self.title = title
        self.data = data
    
    @abstractmethod
    def generate(self):
        """Generate the visualization and return it as a Plotly figure."""
        pass
    
    def to_json(self):
        """Convert the visualization to JSON for web display."""
        fig = self.generate()
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


class LineChart(Visualization):
    """
    Class representing a line chart visualization.
    Inherits from Visualization class, demonstrating inheritance.
    """
    
    def __init__(self, title: str, data: Dict[str, Any]):
        """
        Initialize a LineChart object.
        
        Args:
            title: Title of the line chart
            data: Data to visualize, should contain 'x' and 'y' keys
        """
        super().__init__(title, data)
    
    def generate(self):
        """
        Generate a line chart visualization.
        
        Returns:
            Plotly figure object
        """
        # Check if we have the expected data format
        if 'dates' in self.data and 'scores' in self.data:
            x = self.data['dates']
            y = self.data['scores']
            labels = self.data.get('assessment_names', [])
            
            # Create figure
            fig = go.Figure()
            
            # Add line trace
            fig.add_trace(go.Scatter(
                x=x,
                y=y,
                mode='lines+markers',
                name='Score',
                line=dict(color='royalblue', width=2),
                marker=dict(size=8)
            ))
            
            # Add labels if available
            if labels and len(labels) == len(x):
                for i, (xi, yi, label) in enumerate(zip(x, y, labels)):
                    fig.add_annotation(
                        x=xi,
                        y=yi,
                        text=label,
                        showarrow=True,
                        arrowhead=1,
                        ax=0,
                        ay=-30
                    )
            
            # Update layout
            fig.update_layout(
                title=self.title,
                xaxis_title='Date',
                yaxis_title='Score',
                template='plotly_white',
                hovermode='closest'
            )
            
            return fig
        
        # Fallback for generic x/y data
        elif 'x' in self.data and 'y' in self.data:
            fig = px.line(
                x=self.data['x'],
                y=self.data['y'],
                title=self.title,
                labels={'x': self.data.get('x_label', 'X'), 'y': self.data.get('y_label', 'Y')}
            )
            
            return fig
        
        # Create an empty figure if data format is not recognized
        else:
            fig = go.Figure()
            fig.update_layout(
                title=f"{self.title} (No data)",
                xaxis_title='X',
                yaxis_title='Y'
            )
            
            return fig