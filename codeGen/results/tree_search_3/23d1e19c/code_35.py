from collections import deque

def process_input():
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
    k = int(input())
    path = list(map(int, input().split()))
    
    return n, m, graph, k, path

def solve(n, m, graph, k, path):
    dp = [0]*(n+1)
    for i in range(1, n+1):
        if i not in path:
            max_recompute = 0
            for j in range(i-1, -1, -1):
                if j+1 in graph and i in graph[j+1]:
                    max_recompute = max(max_recompute, dp[j] + 1)
            dp[i] = max_recompute
    return dp[-2], dp[-1]

n, m, graph, k, path = process_input()
print(*solve(n, m, graph, k, path), sep=' ')
