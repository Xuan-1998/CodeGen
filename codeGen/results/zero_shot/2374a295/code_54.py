k, n = map(int, input().split())
dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + (i - 1) * dp[i - 1]) % 1000000007

print((dp[n] * k) % 1000000007)
