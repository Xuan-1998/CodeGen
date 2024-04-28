n, k = map(int, input().split())
dp = [0] * (k + 1)
dp[0] = 1
for i in range(1, n + 1):
    for j in range(min(i, k), -1, -1):
        dp[j] += dp[j - 1]
print(dp[k] % 100000007)
