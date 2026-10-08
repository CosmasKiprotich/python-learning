# Import the random module
import random


# Generate a random 4-digit student ID
def generate_student_id():
    student_id = random.randint(1000, 9999)
    return str(student_id)


# Calculate the average of three marks
def calculate_average(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3
    return average


# Determine the student's grade
def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"