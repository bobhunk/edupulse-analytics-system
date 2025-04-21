import sqlite3
import pandas as pd

# Connect directly to the database
conn = sqlite3.connect('database/edupulse.db')
cursor = conn.cursor()

print("=== Simple Mark Insertion Tool ===")

# Load the CSV file
df = pd.read_csv('sample_marks_2.csv')
print(f"Loaded {len(df)} rows from CSV")

# Hard-coded values
course_id = 3  # DS301

# First, create the assessment if it doesn't exist
assessment_name = "Midterm Exam"
max_score = 100

# Create assessment directly with SQL
cursor.execute("""
INSERT OR IGNORE INTO assessments (course_id, name, type, max_points) 
VALUES (?, ?, ?, ?)
""", (course_id, assessment_name, "Exam", max_score))

# Get the assessment ID
cursor.execute("SELECT id FROM assessments WHERE name = ? AND course_id = ?", 
              (assessment_name, course_id))
result = cursor.fetchone()
if result:
    assessment_id = result[0]
    print(f"Using assessment ID: {assessment_id}")
else:
    print("Failed to get assessment ID")
    exit(1)

# Insert marks for each student
success = 0
for _, row in df.iterrows():
    student_id = int(row['student_id'])
    score = float(row['score'])
    
    print(f"Adding mark for student {student_id}: {score}/{max_score}")
    
    # Insert directly with SQL, replacing if exists
    cursor.execute("""
    INSERT OR REPLACE INTO marks (student_id, assessment_id, score)
    VALUES (?, ?, ?)
    """, (student_id, assessment_id, score))
    
    success += 1

# Commit changes and close
conn.commit()
conn.close()

print(f"Successfully added {success} marks")