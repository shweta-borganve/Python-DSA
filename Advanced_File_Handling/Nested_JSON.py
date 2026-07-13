import json

student = '''
{
"Name":"Shweta" , "Age" : 22 , 
"Adress": {
"City":"Mole", "State":"Karnataka"
          } 
}
'''
data = json.loads(student) 
print(data) 
print(data["Adress"]["State"]) 