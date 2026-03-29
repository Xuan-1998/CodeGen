import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000)

def solve():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    
    edges = []
    index = 2
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        edges.append((a, b))
        index += 2
    
    # Build the adjacency list for the tree
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # DP table: dp[u][d] is the number of vertices at distance d from u
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # To store the result
    result = 0
    
    def dfs(u, parent):
        nonlocal result
        dp[u][0] = 1  # A vertex is at distance 0 from itself
        
        for v in tree[u]:
            if v == parent:
                continue
            dfs(v, u)
            
            # Update result for pairs (u, v) with path length exactly k
            for d in range(1, k + 1):
                if k - d >= 0:
                    result += dp[u][d-1] * dp[v][k-d]
            
            # Combine the dp values of child v into parent u
            for d in range(1, k + 1):
                dp[u][d] += dp[v][d-1]
    
    # Start DFS from an arbitrary root, say vertex 1
    dfs(1, -1)
    
    print(result)

# Call the solve function to execute the solution
solve()

