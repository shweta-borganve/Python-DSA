def generate_hollow_inverted_right_angle_triangle(n):
    result = []

    for i in range(n,0,-1):
        if i == n:
            result.append("*" * n)
        elif i == 2:
            result.append("**") 
        elif i == 1:
            result.append("*") 
        else:
            result.append("*" + " " * (i-2) + "*")
        
    return result
result = generate_hollow_inverted_right_angle_triangle(5)
for row in result:  
    print(row) 