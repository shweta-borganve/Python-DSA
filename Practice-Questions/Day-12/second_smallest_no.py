arr = list(map(int, input("Enter elements: ").split()))
smallest = arr[0]
second_smallest = arr[0] 

for i in arr:
    if i < smallest:
        second_smallest = smallest
        smallest = i 

    elif i > smallest and i < second_smallest:
        second_smallest = i

print("Second_Smallest Element is: ", second_smallest) 