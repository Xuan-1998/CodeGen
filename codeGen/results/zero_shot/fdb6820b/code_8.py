m, N = map(int, input().split())
dp = [0] * (N + 1)
for i in range(m):
    for j in range(N, -1, -1):
        dp[j] += dp[min(j, j-i)] + 1
print(dp[N]%10**9+7)
