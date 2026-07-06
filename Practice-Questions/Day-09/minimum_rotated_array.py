def findMin(nums):
    minimum = nums[0] 

    for num in nums:
        if num < minimum:
            minimum = num

    return minimum 

nums = [4, 5, 6, 7, 0, 1, 2] 

print(findMin(nums)) 