# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

# students = {"Spongebob", "Patrick", "Sandy"}
#
# student = input("Enter student name: ")
#
# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} is not a student")

# grades = {"Sandy": "A",
#           "Spongebob": "B"}
#
# student = input("Enter student name: ")
#
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")


email = "Brocode@gmail.com"

if "@" in email and "." in email:
    print("Email address is valid")
else:
    print("Email address is invalid")