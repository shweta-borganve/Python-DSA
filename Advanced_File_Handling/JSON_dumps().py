import json
student = ([
           {"Name" : "Shweta", "Age" : 22, "City": "Mole"},
           {"Name" : "Tanvi", "Age" : 22, "City": "Ainapur"} 
    
])  

data = json.dumps(student) 
print(data) 