import csv

with open("student.csv", "w", newline = "") as f:
    writer = csv.writer(f) 

    writer.writerow(["Name", "age", "city"])
    writer.writerow(["Shweta", 22, "Mole"])
    writer.writerow(["Tanvi", 22, "Ainapur"])
    writer.writerow(["Pooja", 22, "Ainapur"])
    writer.writerow(["Vinayak", 22, "Kallolli"])
    writer.writerow(["Ujjaif", 22, "Chikkodi"])
    

print("Data written successfully") 

import csv
with open("student.csv", "r") as f:
    reader = csv.reader(f) 

    for row in reader:
        print(row) 