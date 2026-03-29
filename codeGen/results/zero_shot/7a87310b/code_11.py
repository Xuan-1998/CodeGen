import sys

def generate_matrices(n):
    matrices = []
    for a in range(1, n//2 + 1):
        b = n - a
        if a * 2 + b * 2 == n:  # check the trace condition
            d = (a * 2) // 2  # calculate the value of d
            c = b - d
            matrices.append([a, b, c, d])
    return matrices

def is_positive_invertible(matrix):
    a, b, c, d = matrix
    det = a * d - b * c
    return det > 0 and abs(det) == int(det)

def count_matrices(n):
    total_count = 0
    for matrix in generate_matrices(n):
        if is_positive_invertible(matrix):
            total_count += 1
    return total_count

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(count_matrices(n))
