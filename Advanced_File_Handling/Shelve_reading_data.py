import shelve
db = shelve.open("student.db")
db["student1"] = {
    "Name":"Shweta",
    "Age":22,
    "City":"Mole"
}
db.close()
print("Data saved successfully") 

import shelve
db = shelve.open("student.db")
print(db["student1"]) 
db.close() 