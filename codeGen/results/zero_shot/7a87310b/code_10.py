import sys

def generate_matrices():
    matrices = []
    for a in range(1, int(sys.stdin.readline())+1):
        for b in range(a+1, int(sys.stdin.readline())+1):
            c = int(sys.stdin.readline()) - a - b
            d = int(sys.stdin.readline()) - c
            if c >= d:  # ensure determinant is positive
                continue
            matrix = [[a, b], [c, d]]
            matrices.append(matrix)
    return matrices

def is_invertible(matrix):
    det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    return det > 0

matrices = generate_matrices()
count = sum(1 for matrix in matrices if is_invertible(matrix))
print(count)
