"""
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?
"""

def createMatrix(n):
    matrix = []
    ct = 0
    for i in range(0, n):
        new = []
        for j in range(0, n):
            new.append(ct)
            ct += 1
        matrix.append(new)
    return matrix

def rotate(matrix):
    n = len(matrix)
    matrixNew = [[0] * n for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            matrixNew[j][n-i-1] = matrix[i][j]
    return matrixNew

def rotateInPlace(matrix):
    n = len(matrix)
    for layer in range(0, n//2):
        for i in range(layer, n - layer - 1):
            temp = matrix[layer][i]
            matrix[layer][i] = matrix[n-i-1][layer]         #上=左
            matrix[n-i-1][layer] = matrix[n-layer-1][n-i-1] #左=下
            matrix[n-layer-1][n-i-1] = matrix[i][n-layer-1] #下=右
            matrix[i][n-layer-1] = temp                     #右=上
    return matrix

n = 4
matrix = createMatrix(n)

print("before")
for line in matrix:
    print(line)
print("after")
for line in rotate(matrix):
    print(line)
print("after(in-place)")
for line in rotateInPlace(matrix):
    print(line)
