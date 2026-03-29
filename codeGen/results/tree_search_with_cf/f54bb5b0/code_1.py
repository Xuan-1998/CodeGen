import sys
input = sys.stdin.read
from collections import defaultdict

def solve():
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    edges = []
    for i in range(n - 1):
        a, b = int(data[2 + 2 * i]), int(data[3 + 2 * i])
        edges.append((a, b))
    
    # Construct adjacency list
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    # Initialize dp table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base case: each vertex is at distance 0 from itself
    for u in range(1, n + 1):
        dp[u][0] = 1
    
    # DFS function
    def dfs(u, parent):
        # Traverse all children of u
        for v in adj[u]:
            if v == parent:
                continue
            dfs(v, u)
            # Update dp[u] based on dp[v]
            for d in range(1, k + 1):
                dp[u][d] += dp[v][d - 1]
    
    # Calculate the number of valid pairs
    result = [0]
    
    def count_pairs(u, parent):
        # Count pairs with path length exactly k
        for v in adj[u]:
            if v == parent:
                continue
            for d in range(1, k):
                result[0] += dp[v][d - 1] * (dp[u][k - d] - dp[v][k - d - 1])
            count_pairs(v, u)
    
    # Start DFS from vertex 1 (assuming 1 is a valid vertex in the tree)
    dfs(1, -1)
    count_pairs(1, -1)
    
    # Output the result
    print(result[0])

# Run the solve function
if __name__ == "__main__":
    solve()

