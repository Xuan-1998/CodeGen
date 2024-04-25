def count_square_submatrices(N, M, matrix):
    # Initialize the DP table with zeros
    dp = [[0] * M for _ in range(N)]
    count = 0

    # Iterate over the matrix to fill the DP table
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:  # If we're at the top or left edge, the size is 1
                    dp[i][j] = 1
                else:  # Otherwise, take the minimum of the three adjacent cells and add 1
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                count += dp[i][j]  # Add the size of the square to the count

    return count

# Read input from stdin
N, M = map(int, input().split())
matrix = [input().strip() for _ in range(N)]

# Get the count of square submatrices
result = count_square_submatrices(N, M, matrix)

# Print the result to stdout
print(result)
