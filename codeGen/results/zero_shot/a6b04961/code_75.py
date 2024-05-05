import sys
from collections import defaultdict

def read_input():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    return n, m, graph

def solve(n, m, graph):
    # Initialize DP table
    dp = [0] * (n + 1)

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(i - 1, i):
            if j not in graph[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

n, m, graph = read_input()
print(solve(n, m, graph))
