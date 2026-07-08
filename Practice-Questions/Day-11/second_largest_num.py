arr = list(map(int, input("Enter a numbers: ") .split())) 

largest = arr[0]
second_largest = -1

for i in arr:
    if i > largest:
        second_largest = largest
        largest = i

    elif i > second_largest and i != largest:
        second_largest = i

print("Second largest number is: ", second_largest) 