def generate_rectangle(n, m):
    result = [] 
    for i in range(n):
        result.append('*' * m)
    return result 

print((generate_rectangle(5, 10))) 