m, N = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * (N + 1)
dp[0] = 1
for x in arr:
    for i in range(N, x - 1, -1):
        dp[i] += dp[i - x]
print(dp[N]%10**9+7)
