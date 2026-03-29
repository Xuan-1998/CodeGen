import sys

def is_positive_invertible_matrix(matrix):
    # Check if matrix is invertible (i.e., has an inverse)
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        return False
    for i in range(2):
        for j in range(2):
            if matrix[i][j] <= 0:
                return False
    return True

def count_positive_invertible_matrices(N):
    count = 0
    for a in range(1, N+1):  # first element of the matrix
        for b in range(a, N+1):  # second element of the matrix
            for c in range(b, N+1):  # third element of the matrix
                d = N - (a + b + c)  # fourth element of the matrix
                if a * d == b * c and is_positive_invertible_matrix([[a, b], [c, d]]):
                    count += 1
    return count

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(count_positive_invertible_matrices(N))
