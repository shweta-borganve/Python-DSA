arr = list(map(int, input("Enter a numbers: ") .split())) 
min_num = arr[0] 

for i in arr:
    if i < min_num:
        min_num = i

print("Min number is: ", min_num) 