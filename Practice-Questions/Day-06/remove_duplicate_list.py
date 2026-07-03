def remove_duplicates(lst):
    result = []

    for i in range(len(lst)):
        duplicate = False 

        for j in range(len(result)):
            if lst[i] == result[j]:
                duplicate = True
                break 
        if duplicate == False:
            result.append(lst[i]) 

    return result 
print(remove_duplicates([1, 2, 3, 4, 5, 1, 2, 3])) 