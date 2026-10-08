#importing my own module from student_utils.py

import student_utils

student_name = input("Enter Student Name: ").strip()

marks1 = int(input("Enter Marks 1: ").strip())
marks2 = int(input("Enter Marks 2: ").strip())
marks3 = int(input("Enter Marks 3: ").strip())

generated_student_id = student_utils.generate_student_id()
calculate_average = student_utils.calculate_average(marks1, marks2, marks3)
calculate_grade = student_utils.get_grade(calculate_average)

print(f"Marks 1: {marks1}", f"Marks 2: {marks2}", f"Marks 3: {marks3}")
print("--------------------------------------------------------------")

print("-------------Student Details------------")
print("Student ID:", generated_student_id)
print("Student Name:", student_name)
print("Average:", calculate_average)
print("Grade:", calculate_grade)


