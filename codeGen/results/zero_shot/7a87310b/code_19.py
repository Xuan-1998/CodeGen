import sys

def generate_matrices(trace):
    matrices = []
    for i in range(1, trace+1):
        for j in range(i+1, trace+2):
            matrix = [[i, 0], [0, j]]
            matrices.append(matrix)
    return matrices

def is_positive_invertible(matrix):
    eigenvalues = [sum(x) for x in zip(*matrix)]
    if any(eigenvalue <= 0 for eigenvalue in eigenvalues):
        return False
    det = (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
    return det > 0

def count_matrices(trace):
    matrices = generate_matrices(trace)
    count = sum(1 for matrix in matrices if is_positive_invertible(matrix))
    return count

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(count_matrices(N))
