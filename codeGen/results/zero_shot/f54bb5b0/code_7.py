import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

def count_pairs(n, k, edges):
    # Create adjacency list
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # DP table to store the count of paths of different lengths ending at each node
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = [0]  # Use list to pass by reference
    
    def dfs(node, parent):
        # Base case: path of length 0 ending at node is just the node itself
        dp[node][0] = 1
        
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            
            # Count pairs (node, neighbor) where the path length is k
            for length in range(k):
                result[0] += dp[node][length] * dp[neighbor][k - length - 1]
            
            # Update dp table for the current node
            for length in range(1, k + 1):
                dp[node][length] += dp[neighbor][length - 1]
    
    # Start DFS from node 1 (assuming nodes are 1-indexed)
    dfs(1, -1)
    
    return result[0]

if __name__ == "__main__":
    import sys
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

