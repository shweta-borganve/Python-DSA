def generate_square(n):
    result = [] 
    for i in range(n):
        result.append('*' * n)
    return result
print((generate_square(5))) 