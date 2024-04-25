def count_square_submatrices_with_ones_on_diagonal(matrix):
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0]*m for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                count += dp[i][j]
            else:
                dp[i][j] = 0

    return count

# Read input from stdin
n, m = map(int, input().split())
matrix = [input().strip() for _ in range(n)]

# Get the count and print to stdout
count = count_square_submatrices_with_ones_on_diagonal(matrix)
print(count)
