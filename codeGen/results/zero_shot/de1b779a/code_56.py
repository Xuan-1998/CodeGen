import sys

# Read input from stdin
n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(m):
    ai, bi, ci, di = map(int, input().split())
    
    # Fill in the dp table
    for j in range(n, c0 - 1, -1):
        for k in range(m, i - 1, -1):
            if j >= ci and k >= bi:
                dp[j][k] = max(dp[j][k], dp[j - ci][k - bi] + di)
    
# Print the maximum profit
print(max(max(row) for row in dp))
