import sys

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

dp = [[False] * (n + 1) for _ in range(n + 1)]
cost = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i][i] = True
    cost[i] = costs[i - 1]

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        if strings[j].startswith(strings[i]):
            dp[i][j] = dp[i][i + length // 2]
        else:
            dp[i][j] = any(dp[k][j - 1] for k in range(i, j))
        cost[i][j] = min(cost[k][j - 1] if dp[k][j - 1] else float('inf') for k in range(i))

min_cost = sys.maxsize
for i in range(1, n):
    if dp[0][i]:
        min_cost = cost[i]
        break

if min_cost == sys.maxsize:
    print(-1)
else:
    print(min_cost)
