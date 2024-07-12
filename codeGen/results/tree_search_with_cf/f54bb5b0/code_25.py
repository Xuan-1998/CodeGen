import sys
input = sys.stdin.read
from collections import defaultdict

def solve():
    data = input().strip().split()
    n = int(data[0])
    k = int(data[1])
    edges = [(int(data[2 * i + 2]), int(data[2 * i + 3])) for i in range(n - 1)]
    
    # Build the tree using an adjacency list
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # Initialize the dp table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = 1
    
    # Parent array to keep track of the parent nodes
    parent = [-1] * (n + 1)
    
    def dfs(node):
        for neighbor in tree[node]:
            if neighbor == parent[node]:
                continue
            parent[neighbor] = node
            dfs(neighbor)
            for d in range(1, k + 1):
                dp[node][d] += dp[neighbor][d - 1]
    
    # Count the valid pairs
    def count_pairs(node):
        count = 0
        for neighbor in tree[node]:
            if neighbor == parent[node]:
                continue
            for d in range(k):
                count += dp[neighbor][d] * dp[node][k - d - 1]
            count += count_pairs(neighbor)
        return count
    
    # Start DFS from node 1 (assuming 1 is always in the tree)
    parent[1] = -1
    dfs(1)
    
    # Calculate the number of valid pairs
    result = count_pairs(1) // 2  # Each pair is counted twice
    
    print(result)


