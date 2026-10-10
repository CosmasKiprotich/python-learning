
def calculate_average(markk1, markk2, markk3):
    average = (markk1 + markk2 + markk3) / 3
    return average


def get_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"

def get_remark(grade):
    if grade == "A":
         return "Excellent"
    elif grade == "B":
        return "Very Good"
    elif grade == "C":
        return "Good"
    else:
        return "Needs Improvement"

