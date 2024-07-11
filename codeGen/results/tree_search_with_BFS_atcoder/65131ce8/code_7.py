N = int(input())
d = list(map(int,input().split()))
mod = 998244353 

dp = [0]*(N+1)
prefix = [0]*(N+1)
dp[1] = 1

for i in range(2,N+1):
    dp[i] = (dp[i-1]*d[i-2] + prefix[i-1]*(i-d[i-1]))%mod
    prefix[i] = (prefix[i-1] + dp[i])%mod

print(dp[N])

