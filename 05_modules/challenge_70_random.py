# Import the random module
import random

# Ask for the student's name
student_name = input("Enter a student name: ").strip()

# Generate a random student ID between 1000 and 9999
student_id = random.randint(1000, 9999)

# Display the student information
print("Student Name:", student_name)
print("Generated Student ID:", student_id)
