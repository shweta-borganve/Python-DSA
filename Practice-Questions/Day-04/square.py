def generate_square(n):
    result = []

    for i in range(n):
        result.append("*" * n)

    return result
result = generate_square(3)
for row in result:
    print(row) 