def searchMatrix(matrix, target):
    for row in matrix:
        if target in row:
            return True
    return False 

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]] 

print(searchMatrix(matrix, 3))    