python
import sys
input = sys.stdin.read
from collections import defaultdict, deque

def solve():
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    if n == 1:
        print(0)
        return

    edges = list(zip(map(int, data[2::2]), map(int, data[3::2])))
    
    # Create adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # dp[u][d] will store the number of nodes at distance d from node u
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # To avoid counting pairs multiple times
    visited = [False] * (n + 1)
    result = [0]  # Use list to allow modification within nested function
    
    def dfs(u):
        visited[u] = True
        dp[u][0] = 1  # Base case: distance 0 from itself
        
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
                # Update dp[u] using dp[v]
                for d in range(1, k + 1):
                    dp[u][d] += dp[v][d - 1]
        
        # Count pairs with path length k
        for v in graph[u]:
            if visited[v]:
                continue
            for d in range(1, k):
                result[0] += dp[v][d - 1] * (dp[u][k - d] - dp[v][k - d - 1])
    
    # Start DFS from any node, here we choose node 1
    dfs(1)
    
    # Since each pair is counted twice, divide the result by 2
    print(result[0] // 2)

solve()

