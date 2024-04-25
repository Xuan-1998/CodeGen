def count_squares(matrix):
    n, m = len(matrix), len(matrix[0])
    dp = [[0] * m for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                # Check all cells above the main diagonal are ones
                valid = True
                for k in range(1, dp[i][j]):
                    if matrix[i-k][j] == '0':
                        valid = False
                        break
                if valid:
                    count += dp[i][j]
            else:
                dp[i][j] = 0

    return count

# Read input from stdin
N, M = map(int, input().split())
matrix = [input().strip() for _ in range(N)]

# Calculate and print the answer
print(count_squares(matrix))
