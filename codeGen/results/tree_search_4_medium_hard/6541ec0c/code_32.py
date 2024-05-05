import sys
from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    node_values = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dp = [[0]*(k+1) for _ in range(n)]
    for i in range(n):
        if len(graph[i]) == 0:  # leaf node
            xor_value = node_values[i]
            for j in range(k+1):
                if (xor_value ^ node_values[i-1] if i > 0 else 0) == 0:
                    dp[i][j] = 1

    max_j = -1
    for j in range(1, k+1):
        for i in range(n):
            for c in graph[i]:
                for sub_j in range(j-1, 0, -1):
                    if dp[c][sub_j]:
                        dp[i][j] = 1
                        break

    print('YES' if max([j for j in range(k+1) if dp[0][j]]) == k else 'NO')

solve()
