def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(linear_search([23, 45, 12, 67, 34, 89, 10], 67))  
