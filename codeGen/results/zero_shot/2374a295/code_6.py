k = int(input())
n = int(input())
mod = 1000000007
dp = [0]*(k+1)
for i in range(2, k+1):
    dp[i] = (dp[i-1] * i) % mod
print((dp[k] * n) % mod)
