import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

def count_pairs(n, k, edges):
    # Create adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Initialize dp table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = [0]  # Use a list to allow modification inside nested function

    def dfs(node, parent):
        dp[node][0] = 1  # Base case: distance 0 from itself
        
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            # Update dp for the current node using child node's dp
            for d in range(1, k + 1):
                dp[node][d] += dp[neighbor][d - 1]
        
        # Count pairs with exactly k distance
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            for d in range(1, k):
                result[0] += dp[neighbor][d - 1] * (dp[node][k - d] - dp[neighbor][k - d - 1])
        
    dfs(1, -1)
    
    # Each pair is counted twice, so divide by 2
    return result[0] // 2

if __name__ == "__main__":
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
    
    print(count_pairs(n, k, edges))

