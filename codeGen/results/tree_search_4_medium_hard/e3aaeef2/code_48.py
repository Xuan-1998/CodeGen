import sys

# Initialize DP table with base case values
n, m = map(int, input().split())
dp = [[[0 for _ in range(10)] for _ in range(n + 1)] for _ in range(m + 1)]
for i in range(m + 1):
    dp[i][0] = [1 for _ in range(10)]

# Fill the DP table
for i in range(1, m + 1):
    for j in range(1, min(i + 1, n + 1)):
        for k in range(9, -1, -1):
            if (k == 0 and i % 2 == 0) or k < dp[i // 2][j - 1].index(max(dp[i // 2][j - 1])):
                dp[i][j] = [max(k + 1, max(dp[i // 2][j - 1]))]
                break
        else:
            dp[i][j] = dp[i // 2][j - 1]

# Print the final answer
print(max(dp[m][n]))
