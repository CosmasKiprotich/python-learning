# Import functions directly from the package
from student_package import calculate_average, get_grade, get_remark

# Calculate the average marks
average = calculate_average(80, 90, 70)

# Determine the student's grade
grade = get_grade(average)

# Determine the remark to use
remark = get_remark(grade)

# Display the results
print("Average:", average)
print("Grade:", grade)
print("Remark:", remark)