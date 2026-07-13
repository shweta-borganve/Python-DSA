import json
with open("student.json", "r") as f:
    data = json.load(f)
print(data) 
print(data[0] ["Name"])
print(data[0] ["Age"])
print(data[0] ["City"]) 

print(data[1] ["Name"])
print(data[1] ["Age"])
print(data[1] ["City"]) 