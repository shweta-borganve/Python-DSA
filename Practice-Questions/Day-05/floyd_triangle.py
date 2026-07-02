def generate_floyd_triangle(n):
    result = []
    num = 1

    for i in range(1, n+1):
        row = []

        for j in range(i):
            row.append(str(num))
            num += 1
        result.append(" ".join(row)) 

    return result
result = generate_floyd_triangle(5)
for row in result:
    print(row) 

    