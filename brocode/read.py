# Python readin files (.txt, .json, .csv)

file_path = "C:/Users/PRECISION/Desktop/employee.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found")