n = int(input())
dp = [0] * (2 * n + 2)
mod = 998244353

for i in range(n+2):
    for j in range(i):
        if (j & 1) == 0:
            dp[i] += dp[j]
        else:
            dp[i] += dp[j] * 2 % mod
print(dp[n+1])
