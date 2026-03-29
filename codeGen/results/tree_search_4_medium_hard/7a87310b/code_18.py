import sys
from math import comb

def count_invertible_matrices(n):
    total_count = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if is_positive_determinant(i, j):
                total_count += comb(n*(n-1), 2)
    return total_count

def is_positive_determinant(trace_value, matrix_element):
    determinant = (trace_value - matrix_element) * (trace_value - (n-matrix_element))
    return determinant > 0

n = int(sys.stdin.readline())
for _ in range(n):
    N = int(sys.stdin.readline())
    print(count_invertible_matrices(N))
