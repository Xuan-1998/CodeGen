import sys

n = int(input())
dp = {0: 20}
memo = {0: 20}

for _ in range(n):
    t = int(input())
    if t < 90:
        dp[t] = dp[0] + 20
    elif t < 10**9:
        dp[t] = min(dp.get(max(0, t-90), 0) + 50, dp.get(t-14*60, 0) + 120)

print(*dp.values(), sep='\n')
