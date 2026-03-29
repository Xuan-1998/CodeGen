import sys
input = sys.stdin.read
from collections import defaultdict, deque

def solve():
    # Read input
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    # Build the tree
    adj = defaultdict(list)
    index = 2
    for _ in range(n - 1):
        u = int(data[index])
        v = int(data[index + 1])
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # Initialize dp array
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    def dfs(u):
        visited[u] = True
        dp[u][0] = 1
        result = 0
        
        for v in adj[u]:
            if not visited[v]:
                result += dfs(v)
                # Combine dp[u] and dp[v] results
                for d in range(1, k + 1):
                    result += dp[u][d - 1] * dp[v][k - d]
                for d in range(1, k + 1):
                    dp[u][d] += dp[v][d - 1]
        
        return result
    
    # Start DFS from vertex 1 (or any arbitrary vertex)
    result = dfs(1)
    
    # Output the result
    print(result)

solve()

