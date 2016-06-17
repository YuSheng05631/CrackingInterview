"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
"""

def createMatrix(m, n):
    matrix = []
    for i in range(0, m):
        new = []
        for j in range(0, n):
            new.append(1)
        matrix.append(new)
    return matrix

def setZero(matrix):
    row = []
    column = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 0:
                row.append(i)
                column.append(j)
            pass
    for r in row:
        for i in range(0, len(matrix[0])):
            matrix[r][i] = 0
    for c in column:
        for i in range(0, len(matrix)):
            matrix[i][c] = 0
    return matrix

m = 6
n = 5
matrix = createMatrix(m,n)
matrix[1][1] = 0
matrix[3][4] = 0

print("before")
for line in matrix:
    print(line)
print("after")
for line in setZero(matrix):
    print(line)
