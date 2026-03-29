code
from sys import stdin, maxsize

n = int(stdin.readline())
costs = list(map(int, stdin.readline().split()))
strings = [stdin.readline() for _ in range(n)]

dp = [[maxsize] * (max(cost) + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(max(costs) + 1):
        min_cost = maxsize
        if i > 1 and j >= costs[i - 2]:
            min_cost = dp[i - 2][j - costs[i - 2]] + costs[i - 1]
        if i > 0:
            min_cost = min(min_cost, dp[i - 1][j] + (not strings[i - 1] < strings[i - 2]))
        dp[i][j] = min_cost

print(dp[n][max(costs)])
