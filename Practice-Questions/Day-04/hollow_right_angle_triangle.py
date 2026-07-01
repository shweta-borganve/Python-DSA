def generate_hollow_right_angle_triangle(n):
    result = []

    for i in range(1, n+1):
        if i == 1:
            result.append("*")
        elif i == 2:
            result.append("**")
        elif i == n:
            result.append("*" * i)  
        else:
            result.append("*" + " " * (i-2) + "*") 

    return result

result = generate_hollow_right_angle_triangle(5) 
for row in result:
    print(row) 

        