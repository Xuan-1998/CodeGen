import sys
from math import prod

def dfs(n, i, last):
    if n == 0:
        return 1

    res = 0
    for p1, a1, b1 in [(p1, a1, b1) for p1, a1, b1 in zip(probabilities[i:], *zip(*tickets[i:]))]:
        if last < min(a1, b1):
            continue
        prob = (1 - last / 2) ** prod(1 - a1 / 2, 1 - b1 / 2)
        dp[i][j] = prob
        res = max(res, prob)
    return res

n = int(input())
tickets = []
probabilities = []

for _ in range(n):
    p1, a1, b1 = map(float, input().split())
    probabilities.append([p1, 1 - p1])
    tickets.append([a1, b1])

dp = [[0] * (2**20 + 1) for _ in range(50 + 1)]
res = 0

for i in range(n):
    res += dfs(i, i, 0)

print(res)
