
from student_utils import generate_student_id, calculate_average, get_grade

# Calculate the average first
average = calculate_average(85, 90, 80)

# Generate student ID
student_id = generate_student_id()

# Determine grade from the average
grade = get_grade(average)

print("Student ID:", student_id)
print("Average:", average)
print("Grade:", grade)