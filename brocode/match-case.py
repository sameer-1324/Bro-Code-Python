#Match-case statement (switch): An alternative to using many 'elif' statements
#                               Execute some code if a value matches a 'case'
#                               Benefits: cleaner and syntax is more readable
day = int(input("Enter a day (1-7): "))
def day_of_week(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:
            return "Not a valid day"
print("Your day is:", day_of_week(day))