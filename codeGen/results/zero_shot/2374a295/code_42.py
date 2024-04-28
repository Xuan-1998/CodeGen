n, k = map(int, input().split())
dp = [0] * (k + 1)
dp[0] = 1
for i in range(1, k + 1):
    dp[i] = (dp[i - 1] * n) % 1000000007

print(dp[k])
