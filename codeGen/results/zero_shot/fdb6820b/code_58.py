m, N = map(int, input().split())
dp = [0] * (N + 1)
dp[0] = 1
for _ in range(m):
    k = int(input())
    for i in range(N, k - 1, -1):
        dp[i] += dp[i - k]
print(dp[N] % (10**9 + 7))
