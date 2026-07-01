def generate_rectangle(rows, columns):
    result = []

    for i in range(rows):
        result.append("*" * columns)

    return result
result = generate_rectangle(4,5)

for row in result:
    print(row) 