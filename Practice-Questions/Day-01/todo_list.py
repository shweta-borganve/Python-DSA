to_do_list = ["Buy groceries", "Clean the house", "Pay bills", "Finish project"]

to_do_list.append("Call mom")
to_do_list.append("Pay rent")

to_do_list.remove("Clean the house")

if "Pay bills" in to_do_list:
    print("You have bills to pay!") 
else:
    print("No bills to pay!")

print("Your to-do list remains:") 
for task in to_do_list:
    print(task) 