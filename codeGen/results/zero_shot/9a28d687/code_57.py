import sys
from collections import defaultdict

n = int(input())  # read n from input
costs = list(map(int, input().split()))  # read costs from input
strings = [input() for _ in range(n)]  # read strings from input

dp = [[0] * (1 << n) for _ in range(2**n)]
for i in range(2**n):
    dp[i][i] = sum(costs[j] for j in range(n) if ((i >> j) & 1))

for mask in range(1, 2**n):
    for i in range(2**n - 1, mask - 1, -1):
        if (i & mask) == 0:
            continue
        rev_cost = sum(costs[j] for j in range(n) if ((mask >> j) & 1))
        min_cost = float('inf')
        for k in range(i):
            if (k & mask) != 0:
                continue
            min_cost = min(min_cost, dp[k][i - 1] + rev_cost)
        dp[i][i] = min_cost

min_cost = dp[-1][-1]
if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
