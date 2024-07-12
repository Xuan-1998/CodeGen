import sys
input = sys.stdin.read
sys.setrecursionlimit(100000)

def count_pairs(n, k, edges):
    from collections import defaultdict, deque
    
    # Create adjacency list
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # To store the number of valid pairs
    result = 0
    
    # DFS function to traverse the tree and count pairs
    def dfs(node, parent):
        nonlocal result
        # dp[i] will store the number of nodes at distance i from the current node
        dp = [0] * (k + 1)
        dp[0] = 1  # The current node itself is at distance 0
        
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            child_dp = dfs(neighbor, node)
            
            # Count pairs where one node is in the current subtree and the other is in the subtree of the current child
            for i in range(k):
                result += dp[i] * child_dp[k - i - 1]
            
            # Merge child_dp into dp
            for i in range(k):
                dp[i + 1] += child_dp[i]
        
        return dp
    
    # Start DFS from node 1 (assuming 1-based indexing)
    dfs(1, -1)
    
    return result

# Read input
data = input().strip().split()
n = int(data[0])
k = int(data[1])
edges = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(n - 1)]

# Calculate the number of pairs
result = count_pairs(n, k, edges)

# Output the result
print(result)

