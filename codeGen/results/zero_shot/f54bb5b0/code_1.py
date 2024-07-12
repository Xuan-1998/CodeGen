import sys
from collections import defaultdict, deque

def count_pairs_with_path_length_k(n, k, edges):
    # Build the tree as an adjacency list
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # DP table: dp[node][dist] will store the number of nodes at distance `dist` from `node`
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # To store the answer
    result = 0
    
    def dfs(node, parent):
        nonlocal result
        # Initial distance from node to itself is 0
        dp[node][0] = 1
        
        # Traverse all children
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            
            dfs(neighbor, node)
            
            # Count pairs with exact distance k
            for dist1 in range(k):
                for dist2 in range(k - dist1):
                    result += dp[node][dist1] * dp[neighbor][dist2]
            
            # Update dp[node] with information from dp[neighbor]
            for dist in range(k):
                dp[node][dist + 1] += dp[neighbor][dist]
    
    # Start DFS from node 1 (assuming nodes are 1-indexed)
    dfs(1, -1)
    
    return result

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
    
    result = count_pairs_with_path_length_k(n, k, edges)
    print(result)

