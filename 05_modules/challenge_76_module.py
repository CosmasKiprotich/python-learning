
# Define a function to calculate the total marks
def calculate_total(mark1, mark2, mark3):
    return mark1 + mark2 + mark3


# Define a function to display the total
def display_result(total_marks):
    print("Total marks:", total_marks)


# Run this section only when the file is executed directly
if __name__ == "__main__":
    # Calculate and store the total marks
    total = calculate_total(80, 85, 75)

    # Display the total marks
    display_result(total)