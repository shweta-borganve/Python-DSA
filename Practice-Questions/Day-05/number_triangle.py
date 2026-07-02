def generate_number_triangle(n):
    result = []

    for i in range(1, n+1):
        result.append(str(i) * i)

    return result
result = generate_number_triangle(5) 
for row in result:
    print(row) 