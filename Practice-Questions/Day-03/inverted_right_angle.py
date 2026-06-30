def generate_inverted_right_angle_triangle(n):
    result = [] 
    for i in range(n, 0, -1):
        result.append('*' * i)
    return result

print('\n'.join(generate_inverted_right_angle_triangle(3))) 
 