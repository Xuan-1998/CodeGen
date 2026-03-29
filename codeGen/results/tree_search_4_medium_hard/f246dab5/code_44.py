import sys

n = int(input())
dp = [0] * (10**9 + 1)
for _ in range(n):
    t = int(input())
    for i in range(14*60, t+1):
        dp[t] = min(dp[t] if dp[t] > 0 else float('inf'), 
                    dp[i-1] + 20,
                    dp[i-90] + 50,
                    dp[i-1440] + 120)
    print(dp[t])
