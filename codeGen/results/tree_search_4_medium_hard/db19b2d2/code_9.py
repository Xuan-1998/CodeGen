import sys

# Read input from stdin
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Initialize memoization table with zeros
dp = [[0.0 for _ in range(n + 1)] for _ in range(m + 1)]

for i in range(1, m + 1):
    dp[i][0] = 1.0

for j in range(1, n + 1):
    dp[0][j] = 0.0

# Fill up the memoization table
for i in range(1, m + 1):
    for j in range(1, min(i, n) + 1):
        if s[i - 1] >= j:
            dp[i][j] = max(dp[i - 1][j], (s[i - 1] - j + 1) / (i * (m - i)))
        else:
            dp[i][j] = dp[i - 1][j]

# Calculate the final answer
prob = 0.0
for j in range(1, n + 1):
    if s[h - 1] >= j:
        prob += (s[h - 1] - j + 1) / (m * n)

print(prob)
