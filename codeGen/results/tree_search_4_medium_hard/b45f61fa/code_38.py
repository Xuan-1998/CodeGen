code
n = int(input())
p = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 0

for L in range(2, n + 1):
    for i in range(n - L + 1):
        j = i + L - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
            if cost < dp[i][j]:
                dp[i][j] = cost

print(dp[0][n - 1])
