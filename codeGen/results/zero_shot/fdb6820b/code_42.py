m, N = map(int, input().split())
dp = [0] * (N + 1)
dp[0] = 1
for i in range(m):
    for j in range(N, -1, -1):
        if j >= m:
            dp[j] += dp[j - m]
        else:
            break
print(dp[N] % (10**9 + 7))
