def is_positive_invertible_matrix(matrix):
    # Check if the determinant of the matrix is positive
    det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    if det <= 0:
        return False
    
    # Check if the inverse of the matrix exists and is also a positive integer matrix
    inv_matrix = [[(matrix[1][1] / det), (-matrix[0][1] / det)], [(-matrix[1][0] / det), (matrix[0][0] / det)]]
    
    for i in range(2):
        for j in range(2):
            if inv_matrix[i][j] != int(inv_matrix[i][j]) or inv_matrix[i][j] <= 0:
                return False
    
    return True

def count_positive_invertible_matrices(trace):
    count = 0
    for i in range(1, trace + 1):
        if is_positive_invertible_matrix([[i, trace - i], [trace - i, i]]):
            count += 1
    
    return count

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_positive_invertible_matrices(N))
