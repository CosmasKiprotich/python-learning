
# Challenge 86: Class Variables and Class Methods

class SchoolStudent:
    # TODO 1: Create a class variable named school_name
    # Set its initial value to "Python Learning Academy"

    # TODO 2: Create a class variable named student_count
    # Set its initial value to 0

    def __init__(self, name, age):
        # TODO 3: Store name and age as instance variables

        # TODO 4: Increase student_count by 1 whenever
        # a new SchoolStudent object is created
        pass

    def display_details(self):
        # TODO 5: Display the student's name, age,
        # and the shared school name
        pass

    @classmethod
    def change_school_name(cls, new_name):
        # TODO 6: Update the shared school_name using cls
        pass

    @classmethod
    def get_student_count(cls):
        # TODO 7: Return the total number of students created
        pass


if __name__ == "__main__":
    # TODO 8: Create three student objects with different names and ages

    # TODO 9: Display the details of all three students

    # TODO 10: Change the school name using the class method

    # TODO 11: Display the students again to confirm that
    # the new school name applies to every object

    # TODO 12: Print the total number of students created
    pass
