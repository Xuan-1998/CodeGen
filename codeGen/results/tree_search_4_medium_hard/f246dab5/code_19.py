import sys

n = int(sys.stdin.readline().strip())

dp = [0] * (n + 1)
dp[0] = 20

for i in range(1, n + 1):
    min_cost = float('inf')
    
    for t in range(max(0, dp[i-1] - 1439), dp[i-1]):
        cost = min(dp[t], 50) if t >= 90 else dp[t]
        min_cost = min(min_cost, cost + 20)
    
    dp[i] = min_cost

for i in range(n):
    print(dp[i+1], end=' ')
