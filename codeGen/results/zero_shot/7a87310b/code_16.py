import sys

def get_matrix_trace_and_determinant(matrix):
    trace = sum(matrix[i][i] for i in range(2))
    determinant = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    return trace, determinant

def is_positive_invertible(matrix):
    trace, determinant = get_matrix_trace_and_determinant(matrix)
    if trace != N or determinant <= 0:
        return False
    det_inv = 1 / determinant
    matrix_minor = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j == 1:
                    matrix_minor[i][j] = matrix[0][k]*matrix[k][0]
                elif i == 1 and j == 0:
                    matrix_minor[i][j] = matrix[1][k]*matrix[k][1]
            if det_inv * matrix_minor[i][j] <= 0.5:
                return False
    return True

T = int(input())
for _ in range(T):
    N = int(input())
    count = 0
    for i in range(3, min(N+1, 25001)):
        for j in range(i, min(N+1, 25001)):
            matrix = [[i, j], [j, i]]
            if is_positive_invertible(matrix):
                count += 1
    print(count)
