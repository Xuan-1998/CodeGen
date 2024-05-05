code
n, k = map(int, input().split())
s = input()

dp = [[None for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(k+1):
        if i == 0 and j > 0:
            dp[i][j] = s[:j]
        elif i > 0 and j <= n:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] if j > 0 else s[:i])
        elif i > 0 and j == k:
            dp[i][j] = s[:i-1] + s[-1] if i > 1 else s
        elif i == n and j <= n:
            dp[i][j] = s[:j]

print(dp[0][k])
