import shelve
db = shelve.open("student.db")
db["student1"] = {
    "Name":"Shweta",
    "Age":23,
    "City":"Belagavi"
}
db.close()
print("Data updated Successfully") 

import shelve
db = shelve.open("student.db")
print(db["student1"])
db.close() 