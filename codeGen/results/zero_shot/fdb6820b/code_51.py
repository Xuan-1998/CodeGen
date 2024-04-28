m, N = map(int, input().split())
dp = [0] * (N + 1)
dp[0] = 1
for x in range(m):
    for i in range(N, -1, -1):
        if i >= dp[x]:
            dp[i] += dp[i - dp[x]]
print(dp[N] % (10**9 + 7))
