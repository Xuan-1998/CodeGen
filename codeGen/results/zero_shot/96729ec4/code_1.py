def count_square_submatrices(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count = 0
    dp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:  # If we're at the first row or column
                    dp[i][j] = 1
                else:
                    # The size of the square submatrix is limited by the smallest
                    # of the three neighboring cells (top, left, and top-left)
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                # Add the count of square matrices with the current cell as the bottom-right corner
                count += dp[i][j]
    
    return count

# Read input from stdin
N, M = map(int, input().split())
A = [input().strip() for _ in range(N)]

# Get the count of square submatrices and print the result
result = count_square_submatrices(A)
print(result)
