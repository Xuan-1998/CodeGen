n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(m + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif (i & 1) == (j & 1):  # both even or both odd
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

print(dp[n][m])
