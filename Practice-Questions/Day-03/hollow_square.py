def generate_hollow_square(n):
    result = [] 
    for i in range(n):
        if i == 0 or i == n - 1:
            result.append('*' * n)
        else:
            result.append('*' + ' ' * (n - 2) + '*')
    return result

print('\n'.join(generate_hollow_square(5))) 

