import sys
from collections import defaultdict

def min_cost(n, costs, strings):
    dp = {0: 0}
    for i in range(1, n+1):
        dp[i] = float('inf')
        for j in range(i):
            if all(s < t or s == t and len(s) <= len(t) for t in strings[j:i]):
                dp[i] = min(dp[i], dp[j] + costs[i-1])
    return -1 if max(dp.values()) == float('inf') else sum(costs) - max(dp.values())

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]
print(min_cost(n, costs, strings))
