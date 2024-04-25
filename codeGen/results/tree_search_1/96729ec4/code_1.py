n, m = map(int, input().split())
A = [input().strip() for _ in range(n)]

# Initialize the DP array with zeros
dp = [[0] * m for _ in range(n)]
answer = 0

# Fill the DP array
for i in range(n):
    for j in range(m):
        if A[i][j] == '1':
            if i == 0 or j == 0:  # First row or column
                dp[i][j] = 1
            else:
                # Take the minimum of the three previous cells plus 1
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                # Check if the row and column are filled with 1s
                for k in range(1, dp[i][j]):
                    if A[i-k][j] != '1' or A[i][j-k] != '1':
                        dp[i][j] = k
                        break
            answer += dp[i][j]

# Print the answer
print(answer)
