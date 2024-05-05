from collections import defaultdict

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

dp = [[0] * 100001 for _ in range(100001)]
max_length = 0
for i in range(n):
    if len(strings[i]) > max_length:
        max_length = len(strings[i])

memo = defaultdict(int)

def dfs(i, j):
    if memo[(i, j)] != 0:
        return memo[(i, j)]

    if i == 0:
        return 0

    min_cost = float('inf')
    for k in range(j + 1):
        if len(strings[i - 1]) <= k:
            cost = costs[i - 1] * (k - len(strings[i - 1])) + dfs(i - 1, k)
            min_cost = min(min_cost, cost)

    memo[(i, j)] = min_cost
    return min_cost

min_cost = float('inf')
for i in range(1, n + 1):
    min_cost = min(min_cost, dfs(i, max_length))

print(-1 if min_cost == float('inf') else min_cost)
