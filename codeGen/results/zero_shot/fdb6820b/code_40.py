m, N = map(int, input().split())
dp = [0] * (N + 1)
for _ in range(m):
    x = int(input())
    for i in range(N, x - 1, -1):
        dp[i] += dp[i - x]
print(dp[N])
