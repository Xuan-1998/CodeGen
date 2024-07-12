python
import sys
input = sys.stdin.read
from collections import defaultdict, deque

def solve():
    data = input().strip().split()
    n = int(data[0])
    k = int(data[1])
    
    if n == 1:
        print(0)
        return
    
    edges = []
    index = 2
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        edges.append((a, b))
        index += 2
    
    # Build the graph
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # dp[u][d] will store the number of vertices at distance d from u
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = [0]  # Use a list to mutate the count inside dfs
    
    def dfs(u, parent):
        dp[u][0] = 1
        for v in graph[u]:
            if v == parent:
                continue
            dfs(v, u)
            for d in range(k):
                result[0] += dp[u][d] * dp[v][k - d - 1]
            for d in range(1, k + 1):
                dp[u][d] += dp[v][d - 1]
    
    dfs(1, -1)
    print(result[0])


