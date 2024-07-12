python
import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

def count_pairs(n, k, edges):
    # Create adjacency list for the tree
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # dp[u][d] will store the number of vertices at distance d from u
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    def dfs(node, parent):
        # Base case: distance 0 from itself
        dp[node][0] = 1
        
        # Traverse all children (excluding the parent to avoid cycles)
        for child in tree[node]:
            if child == parent:
                continue
            dfs(child, node)
            
            # Update dp[node] based on dp[child]
            for d in range(1, k + 1):
                dp[node][d] += dp[child][d - 1]
    
    # Start DFS from node 1 (assuming 1-based index)
    dfs(1, -1)
    
    # Count the number of pairs with distance exactly k
    result = 0
    
    def count_pairs_dfs(node, parent):
        nonlocal result
        
        # For each child, count pairs where the path goes through the current node
        for child in tree[node]:
            if child == parent:
                continue
            
            # Pairs formed by combining paths from node and child
            for d in range(1, k):
                result += dp[child][d - 1] * (dp[node][k - d] - dp[child][k - d - 1])
            
            count_pairs_dfs(child, node)
    
    count_pairs_dfs(1, -1)
    
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    
    edges = []
    index = 2
    for i in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        edges.append((a, b))
        index += 2
    
    result = count_pairs(n, k, edges)
    print(result)

