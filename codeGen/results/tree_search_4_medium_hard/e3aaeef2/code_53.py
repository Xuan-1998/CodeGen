import sys

t = int(input())

dp = [[0] * (200005) for _ in range(1000001)]

for i in range(t):
    n, m = map(int, input().split())
    
    if n == 1:
        print(1)
    else:
        dp[n][m] = min((dp[k][m-1] + k - (10**(n-1)) + 1) % (10**9+7) for k in range(10**(n-1), 10**n))
        
        print(dp[n][m])
