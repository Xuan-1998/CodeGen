m, N = map(int, input().split())
dp = [0] * (N + 1)
dp[0] = 1
for i in range(m):
    for j in range(N, -1, -1):
        if j >= target[i]:
            dp[j] += dp[j-target[i]]
            dp[j] %= 10**9+7
print(dp[N])
