k = int(input())
n = int(input())

dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[1][1] = 1
for i in range(2, n + 1):
    for j in range(2, min(i + 1, k + 1)):
        dp[i][j] = sum(dp[m][j - 1] for m in range(1, i)) % 1000000007

print(dp[n][k])
