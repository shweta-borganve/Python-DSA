def rotate_list(lst, k):
    for i in range(k):
        last_element = lst.pop()
        lst.insert(0, last_element) 
    return lst

print(rotate_list([23, 45, 12, 67, 34, 89, 10], 3)) 