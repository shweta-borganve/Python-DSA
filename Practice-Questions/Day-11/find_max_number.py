arr = list(map(int, input("Enter a numbers: ") .split())) 
max_num = arr[0] 

for i in arr:
    if i > max_num:
        max_num = i

print("Max number is: ", max_num) 