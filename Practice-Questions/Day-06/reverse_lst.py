def reverse_lst(lst):
    result = []

    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i]) 

    return result

print(reverse_lst([1, 2, 3, 4, 5])) 