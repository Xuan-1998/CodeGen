import math
m, N = map(int, input().split())
dp = [0] * (N+1)
dp[0] = 1
for i in range(1, m+1):
    for j in range(N, 0, -1):
        dp[j] += dp[j-i]
print(dp[N]%10**9+7)
