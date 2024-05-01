import sys
from collections import deque

def read_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    k = int(input())
    path = list(map(int, input().split()))
    return n, m, edges, k, path

def solve(n, m, edges, k, path):
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
    dp = [[0] * (n+1) for _ in range(k+1)]

    queue = deque([(path[0], 0)])
    while queue:
        node, last_computed = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == path[last_computed+1]:
                dp[last_computed+1][neighbor] = min(dp[last_computed][node] + 1, dp[last_computed+1][neighbor])
            else:
                queue.append((neighbor, last_computed))
    return max(max(row) for row in dp), min(min(row) for row in dp)

if __name__ == "__main__":
    n, m, edges, k, path = read_input()
    min_recomputations, max_recomputations = solve(n, m, edges, k, path)
    print(min_recomputations, max_recomputations, end='\n')
