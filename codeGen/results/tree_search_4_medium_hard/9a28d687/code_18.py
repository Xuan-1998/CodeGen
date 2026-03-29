import sys

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

max_cost = max(costs)
dp = [[0] * (max_cost + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(max_cost + 1):
        if strings[i - 1] < strings[i]:
            dp[i][j] = dp[i - 1][j]
        elif costs[i - 1] <= j:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - costs[i - 1]] + costs[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

if dp[n][max_cost] >= sum(costs):
    print(dp[n][max_cost])
else:
    print(-1)
