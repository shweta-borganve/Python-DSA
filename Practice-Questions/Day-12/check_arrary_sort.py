arr = list(map(int, input("Enter Elements: ") .split())) 

sorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i+1]:
        sorted = False
        break

if sorted:
    print("Array is sorted")

else:
    print("Array is not sorted") 