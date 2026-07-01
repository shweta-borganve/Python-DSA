def generate_hollow_square(n):
    result = []
    
    for i in range(n):
        if i == 0 or i == n-1:
            result.append("*" * n) 
        else:
            result.append("*" + " " * (n-2) + "*") 
            
    return result
        
result = generate_hollow_square(5) 
for row in result:
    print(row) 