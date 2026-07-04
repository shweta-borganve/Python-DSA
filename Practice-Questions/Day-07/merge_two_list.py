def merge_list(list1, list2):
    result = list1 + list2
    result.sort()
    return result
print(merge_list([23, 45, 12, 67, 34, 89, 10], [5, 15, 25, 35]))
