import json
student = ([
           {"Name" : "Shweta", "Age" : 22, "City": "Mole"},
           {"Name" : "Tanvi", "Age" : 22, "City": "Ainapur"} 
    
])     

with open("student.json", "w") as f:
    json.dump(student, f, indent = 4) 

print("Data written successfully") 