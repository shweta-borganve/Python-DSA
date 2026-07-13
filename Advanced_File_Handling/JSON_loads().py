import json

student = [
    '{"Name": "Shweta", "Age": 22, "City": "Mole"}',
    '{"Name": "Tanvi", "Age": 22, "City": "Ainapur"}'
]

for i in student:
    data = json.loads(i)
    print(data)