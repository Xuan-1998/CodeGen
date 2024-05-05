===BEGIN CODE===
n = int(input())
costs = [int(x) for x in input().split()]
strings = [input() for _ in range(n)]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i):
        if strings[i - 1] < strings[j]:
            dp[i][j] = min(dp[i - 1][j], costs[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]
    for k in range(j + 1, i):
        dp[i][k] = dp[i][k]

min_cost = float('inf')
for j in range(n):
    if strings[j] != strings[0]:
        min_cost = min(min_cost, costs[j])

print(min_cost) if min_cost != float('inf') else print(-1)
===END CODE===
