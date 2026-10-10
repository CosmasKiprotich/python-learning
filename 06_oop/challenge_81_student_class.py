
# ============================================================
# CHALLENGE 81: BASIC STUDENT CLASS
# Learn: Classes, objects, attributes, methods, and self
# ============================================================

class Student:
    # Initialize each student object with a name and three marks
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    # Calculate and return the student's average mark
    def calculate_average(self):
        average = (self.mark1 + self.mark2 + self.mark3) / 3
        return average

    # Determine the grade using the student's average
    def get_grade(self):
        average = self.calculate_average()

        if average >= 70:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 50:
            return "C"
        else:
            return "F"

    # Display the student's information
    def display_details(self):
        print("------ Student Details ------")
        print("Name:", self.name)
        print("Average:", self.calculate_average())
        print("Grade:", self.get_grade())


# ============================================================
# CHALLENGE 82: INHERITANCE
# Learn: Child classes, super(), and method overriding
# ============================================================

class GraduateStudent(Student):
    # Add a research topic to the attributes inherited from Student
    def __init__(self, name, mark1, mark2, mark3, research_topic):
        # Call the parent constructor to initialize student information
        super().__init__(name, mark1, mark2, mark3)

        # Store the additional attribute for graduate students
        self.research_topic = research_topic

    # Override the parent's display_details() method
    def display_details(self):
        # Reuse the parent's method instead of duplicating its code
        super().display_details()

        # Display the additional graduate-student information
        print("Research Topic:", self.research_topic)


# ============================================================
# CHALLENGE 84: ENCAPSULATION
# Learn: Name-mangled attributes and controlled mark updates
# ============================================================

class EncapsulatedStudent:
    def __init__(self, name, mark1, mark2, mark3):
        # The name remains a regular public attribute
        self.name = name

        # Double underscores trigger Python's name-mangling mechanism
        # to discourage direct access to these attributes
        self.__mark1 = mark1
        self.__mark2 = mark2
        self.__mark3 = mark3

    # Calculate the average using the encapsulated marks
    def get_average(self):
        average = (self.__mark1 + self.__mark2 + self.__mark3) / 3
        return average

    # Determine the grade using the calculated average
    def get_grade(self):
        average = self.get_average()

        if average >= 70:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 50:
            return "C"
        else:
            return "F"

    # Update marks only after validating all proposed values
    def update_marks(self, mark1, mark2, mark3):
        # Collect the proposed marks for validation
        new_marks = [mark1, mark2, mark3]

        # Check each mark before changing the existing values
        for mark in new_marks:
            # Reject non-numeric values, Boolean values, and out-of-range marks
            if (
                not isinstance(mark, (int, float))
                or isinstance(mark, bool)
                or not 0 <= mark <= 100
            ):
                print("Invalid mark. Marks must be between 0 and 100.")
                return  # Stop without changing any existing marks

        # Update the marks only when all three values are valid
        self.__mark1 = mark1
        self.__mark2 = mark2
        self.__mark3 = mark3

        print("Marks updated successfully.")


# ============================================================
# CHALLENGE 83: POLYMORPHISM
# Learn: Calling the same method on different object types
# ============================================================
# Polymorphism is demonstrated in the main program below.
# Student and GraduateStudent objects both support display_details(),
# but the graduate student also displays a research topic.


# ============================================================
# CHALLENGE 85: INHERITANCE + ENCAPSULATION
# Learn: Extending an encapsulated parent class
# ============================================================

class EncapsulatedGraduateStudent(EncapsulatedStudent):
    def __init__(self, name, mark1, mark2, mark3, research_topic):
        # Initialize the inherited name and marks
        super().__init__(name, mark1, mark2, mark3)

        # Store the research topic using name-mangling
        self.__research_topic = research_topic

    # Provide controlled access to the research topic
    def get_research_topic(self):
        return self.__research_topic

    # Display information using methods inherited from the parent
    def display_details(self):
        print("------ Graduate Student Details ------")
        print("Name:", self.name)
        print("Average:", self.get_average())
        print("Grade:", self.get_grade())

        # Access the research topic through its getter method
        print("Research Topic:", self.get_research_topic())


# ============================================================
# MAIN PROGRAM
# Learn: Creating objects, calling methods, and polymorphism
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # CHALLENGE 81 AND 82: Create student objects
    # --------------------------------------------------------

    student1 = Student("Alice", 80, 75, 90)
    student2 = Student("Brian", 55, 60, 50)

    # Create a graduate student with an additional research topic
    student3 = GraduateStudent(
        "Charles", 55, 60, 50, "Effects of AI on youths"
    )

    # --------------------------------------------------------
    # CHALLENGE 83: Demonstrate polymorphism
    # --------------------------------------------------------

    # The list contains both Student and GraduateStudent objects
    student_list = [student1, student2, student3]

    # Call the same method on each object
    # Python uses the appropriate version of display_details()
    for student in student_list:
        student.display_details()
        print()  # Add a blank line between students

    # --------------------------------------------------------
    # CHALLENGE 84: Demonstrate encapsulation
    # --------------------------------------------------------

    student4 = EncapsulatedStudent("Alice", 80, 75, 90)

    # Access the public name and use methods to read the marks' results
    print("------ Encapsulated Student ------")
    print("Name:", student4.name)
    print("Average:", student4.get_average())
    print("Grade:", student4.get_grade())

    # Test a valid mark update
    student4.update_marks(85, 90, 95)
    print("Updated average:", student4.get_average())

    # Test an invalid update; no marks should change
    student4.update_marks(85, 120, 95)
    print("Average after invalid update:", student4.get_average())

    # --------------------------------------------------------
    # CHALLENGE 85: Combine inheritance and encapsulation
    # --------------------------------------------------------

    student5 = EncapsulatedGraduateStudent(
        "Cosmas",
        85,
        80,
        90,
        "Effects of AI on Youths"
    )

    # Display inherited student information and the research topic
    student5.display_details()
