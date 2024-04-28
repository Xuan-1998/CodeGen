m, N = map(int, input().split())
dp = [0] * (N + 1)
dp[0] = 1
for x in map(int, input().split()):
    for i in range(N + 1):
        if i >= x:
            dp[i] += dp[i - x]
print(dp[N]%10**9+7)
