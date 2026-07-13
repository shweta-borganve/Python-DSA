import csv
with open("student.csv", "w", newline="") as f:
    fieldnames = ["Name", "age", "city"]

    writer = csv.DictWriter(f, fieldnames = fieldnames) 
    writer.writeheader() 
    writer.writerows([
        {"Name" : "Shweta", "age" : 22, "city" : "Mole"},
        {"Name" : "Tanvi", "age" : 22, "city" : "Ainapur"},
        {"Name" : "Pooja", "age" : 22, "city" : "Ainapur"}
    ]) 

print("Data written Successfully") 
        