m, N = map(int, input().split())
dp = [0] * (N + 1)
for i in range(m):
    for j in range(N, arr[i], -1):
        dp[j] += dp[j-arr[i]]
print(dp[N]%10**9+7)
