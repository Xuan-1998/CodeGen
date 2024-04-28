m, N = map(int, input().split())
dp = [0] * (N + 1)
dp[0] = 1
for i in range(m):
    for j in range(N, -1, -1):
        dp[j] += dp[min(j, N - i)]
    dp[N % (10**9 + 7)] = dp[N % (10**9 + 7)] % (10**9 + 7)
print(dp[-1])
