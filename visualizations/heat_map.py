import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import json
from typing import Dict, List, Any

from visualizations.line_chart import Visualization

class HeatMap(Visualization):
    """
    Class representing a heat map visualization.
    Inherits from Visualization class, demonstrating inheritance.
    """
    
    def __init__(self, title: str, data: Dict[str, Any]):
        """
        Initialize a HeatMap object.
        
        Args:
            title: Title of the heat map
            data: Data to visualize, should contain appropriate format for heatmap
        """
        super().__init__(title, data)
    
    def generate(self):
        """
        Generate a heat map visualization.
        
        Returns:
            Plotly figure object
        """
        # Check if we have the expected data format for student performance
        if 'assessment_names' in self.data and 'score_distribution' in self.data:
            # Create a heatmap for grade distribution
            grade_categories = ['A', 'B', 'C', 'D', 'F']
            values = [self.data['score_distribution'].get(grade, 0) for grade in grade_categories]
            
            fig = go.Figure(data=go.Heatmap(
                z=[values],
                x=grade_categories,
                y=[self.title],
                colorscale='RdYlGn',
                reversescale=True,
                text=[values],
                texttemplate="%{text}%",
                showscale=False
            ))
            
            # Update layout
            fig.update_layout(
                title=self.title,
                xaxis_title='Grade',
                yaxis_title='',
                template='plotly_white'
            )
            
            return fig
        
        # Check if we have matrix data format
        elif 'matrix' in self.data and 'x_labels' in self.data and 'y_labels' in self.data:
            fig = go.Figure(data=go.Heatmap(
                z=self.data['matrix'],
                x=self.data['x_labels'],
                y=self.data['y_labels'],
                colorscale='RdYlGn',
                reversescale=True if self.data.get('reverse_scale', False) else False,
                showscale=True
            ))
            
            # Update layout
            fig.update_layout(
                title=self.title,
                xaxis_title=self.data.get('x_title', 'X'),
                yaxis_title=self.data.get('y_title', 'Y'),
                template='plotly_white'
            )
            
            return fig
        
        # If we have student performance data
        elif 'students' in self.data and 'assessments' in self.data and 'scores' in self.data:
            # Create a heatmap for student performance
            fig = go.Figure(data=go.Heatmap(
                z=self.data['scores'],
                x=self.data['assessments'],
                y=self.data['students'],
                colorscale='RdYlGn',
                zmin=0,
                zmax=100,
                showscale=True,
                colorbar=dict(title='Score %')
            ))
            
            # Update layout
            fig.update_layout(
                title=self.title,
                xaxis_title='Assessment',
                yaxis_title='Student',
                template='plotly_white'
            )
            
            return fig
        
        # Create a sample heatmap if data format is not recognized
        else:
            # Generate some random data
            x_labels = ['Assessment 1', 'Assessment 2', 'Assessment 3', 'Assessment 4']
            y_labels = ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5']
            
            # Create random scores between 50 and 100
            np.random.seed(42)  # For reproducibility
            scores = np.random.randint(50, 100, size=(len(y_labels), len(x_labels)))
            
            fig = go.Figure(data=go.Heatmap(
                z=scores,
                x=x_labels,
                y=y_labels,
                colorscale='RdYlGn',
                zmin=0,
                zmax=100,
                showscale=True,
                colorbar=dict(title='Score %')
            ))
            
            # Update layout
            fig.update_layout(
                title=f"{self.title} (Sample Data)",
                xaxis_title='Assessment',
                yaxis_title='Student',
                template='plotly_white'
            )
            
            return fig