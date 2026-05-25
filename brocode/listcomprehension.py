# list comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# doubles = [x * 2 for x in range(1, 11)]
#
# print(doubles)

# fruits = ["apple", "banana", "cherry"]
# fruits_chars = [fruit[0] for fruit in fruits]

# numbers = [1, -2, 3, -4, 5, -6]
# positive_nums = [num for num in numbers if num>=0]
#
# print(positive_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)