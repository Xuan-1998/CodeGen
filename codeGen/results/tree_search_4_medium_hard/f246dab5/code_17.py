import sys

n = int(input())
trips = []
for _ in range(n):
    trips.append(int(input()))

dp = [0] * 10**9
for i, t in enumerate(trips):
    if t < 90:
        dp[t] = min(dp.get(t-1, float('inf')) + 20, dp[0] + 50)
    elif t < 10*90+1:
        dp[t] = min(dp.get(t-1, float('inf')) + 20, dp.get(t-90, float('inf')) + 120)
    else:
        dp[t] = dp.get(t-1, 0) + 20
print(*dp[:n], sep='\n')
