def generate_right_angle_triangle(n):
    result = []
    for i in range(n):
        spaces = " " * i
        stars = "*" * (2*(n-i)-1) 
        result.append(spaces + stars + spaces) 

    for i in range(1, n):
        spaces = " " * (n-i-1)
        stars = "*" * (2*i+1)
        result.append(spaces + stars + spaces) 

    return result 
result = generate_right_angle_triangle(5)
for row in result:  
    print(row) 