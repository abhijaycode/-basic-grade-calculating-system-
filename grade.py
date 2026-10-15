# Input marks from the user
marks = float(input("Enter the marks: "))

# Grading logic
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 50:
    grade = "E"
else:
    grade = "F"

# Display the output
print(f"Grade: {grade}")


# Input marks from the user
marks = float(input("Enter the marks: "))

# Apply the modification rule only if marks are 50 or above
if marks >= 50:
    # Find the next higher multiple of 10
    remainder = marks % 10
    if remainder != 0:
        next_multiple_of_10 = marks + (10 - remainder)
        difference = next_multiple_of_10 - marks
        
        # If the difference is less than 3, upgrade the marks
        if difference < 3:
            marks = next_multiple_of_10

# Grading logic using the modified marks
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 50:
    grade = "E"
else:
    grade = "F"

# Display the final grade
print(f"Final Grade: {grade}")
