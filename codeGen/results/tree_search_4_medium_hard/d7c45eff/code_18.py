code
n, k = map(int, input().split())
s = input()

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][1] = s[:i]

for j in range(2, k + 1):
    for i in range(j, n + 1):
        if i < n:
            dp[i][j] = min(dp[i - 1][j], s[:i])
        else:
            dp[i][j] = s

print(dp[n][k])
