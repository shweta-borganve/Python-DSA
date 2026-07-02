def generate_invert_pyramid(n):
    result = []

    for i in range(n):
        spaces = " " * i
        stars = "*" *(2*(n-i)-1)
        result.append(spaces+stars+spaces)

    return result
result = generate_invert_pyramid(5) 
for row in result:
    print(row) 


