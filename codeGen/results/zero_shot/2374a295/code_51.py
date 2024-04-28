n, k = map(int, input().split())
dp = [0] * (k + 1)
dp[0] = 1
for i in range(1, n):
    for j in range(min(i+1, k), -1, -1):
        dp[j] = (dp[j] + dp[j-1]) % 1000000007
print(dp[-1])
