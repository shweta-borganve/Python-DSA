inventory = ["Apples", "Bananas", "Oranges"]
inventory.append("Grapes")
inventory.append("chikku") 
print(inventory) 

item = "Oranges"
if item in inventory:
    print(f"{item} is available in the inventory.")
else:
    print(f"{item} is not available in the inventory.") 

print("Current inventory:") 
for item in inventory:
    print(item) 