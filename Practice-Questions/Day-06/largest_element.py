def largest_element(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
    return largest 

print(largest_element([1, 2, 3, 4, 5])) 