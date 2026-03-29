import sys
input = sys.stdin.read
from collections import defaultdict, deque

def solve():
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
    
    # DP table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # To store the number of valid pairs
    result = 0
    
    def dfs(node, parent):
        nonlocal result
        dp[node][0] = 1
        
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            
            # Count pairs between node and neighbor
            for d in range(k):
                result += dp[node][d] * dp[neighbor][k - d - 1]
            
            # Update dp[node] using dp[neighbor]
            for d in range(k):
                dp[node][d + 1] += dp[neighbor][d]
    
    # Start DFS from node 1 (or any node, since it's a tree)
    dfs(1, -1)
    
    print(result)

# Call the solve function
solve()

