import sys
input = sys.stdin.read
from collections import defaultdict, deque

def solve():
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    if k == 0:
        print(0)
        return
    
    edges = list(zip(map(int, data[2::2]), map(int, data[3::2])))
    
    # Build the adjacency list for the tree
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    # Initialize the result counter
    result = 0
    
    # Function to perform DFS and calculate pairs with distance k
    def dfs(node, parent):
        nonlocal result
        dp = [0] * (k + 1)
        dp[0] = 1
        
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            child_dp = dfs(neighbor, node)
            
            # Count pairs where one node is in the current subtree and the other in the rest of the tree
            for i in range(k):
                result += dp[i] * child_dp[k - 1 - i]
            
            # Update the dp table for the current node
            for i in range(k):
                dp[i + 1] += child_dp[i]
        
        return dp
    
    # Start DFS from node 1 (assuming 1-based indexing)
    dfs(1, -1)
    
    print(result)

# Call the solve function
solve()

