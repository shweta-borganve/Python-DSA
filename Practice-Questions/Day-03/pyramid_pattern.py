def generate_pyramid_pattern(n):
    result = [] 
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        result.append(spaces + stars + spaces)
    return result 

print('\n'.join(generate_pyramid_pattern(5))) 