// EduPulse Dashboard JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Handle chart rendering
    renderCharts();
    
    // Handle tab switching
    const tabElements = document.querySelectorAll('button[data-bs-toggle="tab"]');
    tabElements.forEach(tab => {
        tab.addEventListener('shown.bs.tab', event => {
            // Re-render charts when tab is shown to fix layout issues
            renderCharts();
        });
    });
});

// Function to render all charts on the page
function renderCharts() {
    // Find all chart containers
    const chartContainers = document.querySelectorAll('.chart-container');
    
    chartContainers.forEach(container => {
        const chartType = container.dataset.chartType;
        const chartData = JSON.parse(container.dataset.chartData);
        
        if (chartType && chartData) {
            renderChart(container.id, chartType, chartData);
        }
    });
}

// Function to render a specific chart
function renderChart(containerId, chartType, chartData) {
    const container = document.getElementById(containerId);
    
    if (!container) return;
    
    switch (chartType) {
        case 'line_chart':
            renderLineChart(container, chartData);
            break;
        case 'bar_chart':
            renderBarChart(container, chartData);
            break;
        case 'heat_map':
            renderHeatMap(container, chartData);
            break;
        default:
            console.error('Unknown chart type:', chartType);
    }
}

// Render line chart
function renderLineChart(container, chartData) {
    Plotly.newPlot(container, [chartData.data], chartData.layout);
}

// Render bar chart
function renderBarChart(container, chartData) {
    // Create a trace for the bar chart
    const trace = {
        x: chartData.labels || [],
        y: chartData.values || [],
        type: 'bar',
        marker: {
            color: 'rgba(55, 128, 191, 0.7)',
            line: {
                color: 'rgba(55, 128, 191, 1.0)',
                width: 2
            }
        }
    };
    
    // Create layout
    const layout = {
        title: 'Course Performance',
        xaxis: {
            title: 'Course'
        },
        yaxis: {
            title: 'Performance (%)',
            range: [0, 100]
        },
        margin: {
            l: 50,
            r: 50,
            b: 100,
            t: 50,
            pad: 4
        }
    };
    
    // Render the chart
    Plotly.newPlot(container, [trace], layout);
}

// Render heat map
function renderHeatMap(container, chartData) {
    Plotly.newPlot(container, [chartData.data], chartData.layout);
}

// Handle student search
const studentSearchForm = document.getElementById('student-search-form');
if (studentSearchForm) {
    studentSearchForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const studentId = document.getElementById('student-id').value;
        window.location.href = `/student/${studentId}`;
    });
}

// Handle course search
const courseSearchForm = document.getElementById('course-search-form');
if (courseSearchForm) {
    courseSearchForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const courseId = document.getElementById('course-id').value;
        window.location.href = `/course/${courseId}`;
    });
}