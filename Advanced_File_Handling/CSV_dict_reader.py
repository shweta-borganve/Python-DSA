import csv
with open("student.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row) 

import csv
with open("student.csv","r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row["Name"])
        print(row["age"])
        print(row["city"])  