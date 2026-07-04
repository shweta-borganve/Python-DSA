def merge_list(lst1, lst2):
    result = []

    for num in lst1:
        result.append(num)

    for num in lst2:
        result.append(num) 

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                temp = result[i] 
                result[i] = result[j] 
                result[i] = temp
    return result
print(merge_list([23, 45, 12, 67, 34, 89, 10], [5, 15, 25, 35]))
