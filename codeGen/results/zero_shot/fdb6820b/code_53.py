m, N = map(int, input().split())
dp = [0] * (N + 1)
dp[0] = 1
for _ in range(m):
    n = int(input())
    for i in range(N, n - 1, -1):
        dp[i] += dp[i - n]
print(dp[N] % (10**9 + 7))
