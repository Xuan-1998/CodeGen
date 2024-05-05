import sys

n, m = map(int, input().split())
dp = [0] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    if i == 0:  # Initialize dp[0]
        dp[0] = 0
    else:
        for j in range(1, n + 1):  # Update dp[j] based on the previous edge
            if j == u or j == v:  # Edge (u, v) ends at vertex j
                dp[j] = max(dp[j - 1] * (j + 1), min((v - u) // 2 + 1, dp[u - 1] * (u + 1)))
    if i > 0:  # Update dp[n]
        dp[n] = max(dp[n - 1] * (n + 1), min((v - 1) // 2 + 1, dp[v - 1] * (v + 1)))

print(max(0, dp[-1]))
