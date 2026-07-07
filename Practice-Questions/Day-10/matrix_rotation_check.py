def rotate(matrix):
    n = len(matrix) 
    return [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)] 

def findRotation(mat, target):
    for i in range(4):
        if mat == target:
            return True
        mat = rotate(mat) 
    return False 

mat = [[0,1],[1,0]]
target = [[1,0],[0,1]] 

print(findRotation(mat, target)) 