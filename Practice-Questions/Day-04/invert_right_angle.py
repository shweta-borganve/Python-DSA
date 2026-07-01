def generate_inverse_right_angle_triangle(n):
    result = []
    
    for i in range(n , 0 , -1):
        result.append("*" * i)
        
    return result
    
result = generate_inverse_right_angle_triangle(5)
print(result)

for row in result:
    print(row) 