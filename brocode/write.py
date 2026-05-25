# Python writing files (.txt, .json, .csv)
import csv

employee = [["Name", "Age", "Salary"],
            ["Spongebob", 30, 100],
            ["Patrick", 37, 0],
            ["Sandy", 27, 200]]
file_path = "output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' created")
except FileExistsError:
    print("That file already exists")