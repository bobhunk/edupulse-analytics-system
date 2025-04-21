import plotly.graph_objects as go
import plotly.express as px
import json
from typing import Dict, List, Any

from visualizations.line_chart import Visualization

class BarChart(Visualization):
    """
    Class representing a bar chart visualization.
    Inherits from Visualization class, demonstrating inheritance.
    """
    
    def __init__(self, title: str, data: Dict[str, Any]):
        """
        Initialize a BarChart object.
        
        Args:
            title: Title of the bar chart
            data: Data to visualize, should contain 'x' and 'y' keys or specific attendance data
        """
        super().__init__(title, data)
    
    def generate(self):
        """
        Generate a bar chart visualization.
        
        Returns:
            Plotly figure object
        """
        # Check if we have attendance data format
        if 'present_count' in self.data and 'late_count' in self.data and 'absent_count' in self.data:
            # Create attendance bar chart
            categories = ['Present', 'Late', 'Absent']
            values = [self.data['present_count'], self.data['late_count'], self.data['absent_count']]
            colors = ['#4CAF50', '#FFC107', '#F44336']  # Green, Yellow, Red
            
            fig = go.Figure()
            
            # Add bar trace
            fig.add_trace(go.Bar(
                x=categories,
                y=values,
                marker_color=colors,
                text=values,
                textposition='auto'
            ))
            
            # Add attendance rate as annotation
            if 'attendance_rate' in self.data:
                fig.add_annotation(
                    x=0.5,
                    y=1.1,
                    xref='paper',
                    yref='paper',
                    text=f"Attendance Rate: {self.data['attendance_rate']:.1f}%",
                    showarrow=False,
                    font=dict(size=14)
                )
            
            # Update layout
            fig.update_layout(
                title=self.title,
                xaxis_title='Status',
                yaxis_title='Count',
                template='plotly_white'
            )
            
            return fig
        
        # Check if we have assessment data format
        elif 'assessment_names' in self.data and 'average_scores' in self.data:
            x = self.data['assessment_names']
            y = self.data['average_scores']
            
            fig = go.Figure()
            
            # Add bar trace
            fig.add_trace(go.Bar(
                x=x,
                y=y,
                marker_color='royalblue',
                text=[f"{score:.1f}" for score in y],
                textposition='auto'
            ))
            
            # Update layout
            fig.update_layout(
                title=self.title,
                xaxis_title='Assessment',
                yaxis_title='Average Score',
                template='plotly_white'
            )
            
            return fig
        
        # Fallback for generic x/y data
        elif 'x' in self.data and 'y' in self.data:
            fig = px.bar(
                x=self.data['x'],
                y=self.data['y'],
                title=self.title,
                labels={'x': self.data.get('x_label', 'X'), 'y': self.data.get('y_label', 'Y')},
                color_discrete_sequence=['royalblue']
            )
            
            # Add text labels on bars
            fig.update_traces(
                texttemplate='%{y:.1f}',
                textposition='auto'
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