def selection_sort(lst):
    lst = [64, 25, 12, 22, 11] 
    for i in range(len(lst)):
        m = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[m]:
                m = j
        lst[i], lst[m] = lst[m], lst[i] 
    return lst

print(selection_sort([23, 45, 12, 67, 34, 89, 10])) 