def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i 
        
    return -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(search(nums, target)) 