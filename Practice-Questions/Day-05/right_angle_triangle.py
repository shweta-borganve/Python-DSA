def generate_right_angle_triangle(n):
    result = []

    for i in range(1, n+1):
        spaces = " " * (n-i)
        stars = "*" * i
        result.append(spaces + stars + spaces) 

    return result
result = generate_right_angle_triangle(5)
for row in result:
    print(row)  