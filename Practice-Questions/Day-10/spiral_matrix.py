def spiralOrder(matrix):
    ans = []

    while matrix:
        ans += matrix.pop(0)

        matrix = list(zip(*matrix))[::-1] 

    return ans 

matrix = [[1,2,3],[4,5,6],[7,8,9]] 
print(spiralOrder(matrix)) 