n, k = map(int, input().split())
dp = [0] * (k + 1)
dp[0] = 1
for i in range(1, k + 1):
    dp[i] = dp[i - 1]
    for j in range(i):
        if n // dp[j] >= dp[i - j - 1]:
            dp[i] += dp[j]
print(dp[k] % 1000007)
