def generate_number_pyramid(n):
    result = []
    for i in range(1, n+1):
        spaces = " " * (n - i)
        numbers = " ".join(str(num) for num in range(1, i + 1)) 
        result.append(spaces + numbers + spaces)
    return result
result = generate_number_pyramid(5)
for row in result:
    print(row) 