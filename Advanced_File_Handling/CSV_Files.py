import csv

with open("student.csv", "w", newline = "") as f:
    writer = csv.writer(f) 

    writer.writerow(["Name", "age", "city"])
    writer.writerow(["Shweta", 22, "Bangalore"])
    writer.writerow(["Tanvi", 22, "Belagavi"])
    writer.writerow(["Pooja", 22, "Belagavi"])

print("Data written successfully") 

import csv

with open("student.csv", "r") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row) 
