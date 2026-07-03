def all_unique(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True 

print(all_unique([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])) 
print(all_unique([1, 2, 3, 4, 5])) 