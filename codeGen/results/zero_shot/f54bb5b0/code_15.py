python
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000)

def count_pairs(n, k, edges):
    # Create adjacency list for the tree
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    def dfs(node, parent):
        # dp[node][d] will store the number of nodes at distance d from node
        dp = [0] * (k + 1)
        dp[0] = 1  # Distance to itself is 0
        
        total_pairs = 0
        
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            child_dp, child_pairs = dfs(neighbor, node)
            total_pairs += child_pairs
            
            # Count pairs where one node is in the subtree of `neighbor` and the other node is in the subtree of `node`
            for i in range(k):
                total_pairs += dp[i] * child_dp[k - i - 1]
            
            # Combine child_dp into dp
            for i in range(k):
                dp[i + 1] += child_dp[i]
        
        return dp, total_pairs
    
    _, result = dfs(1, -1)
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
    
    result = count_pairs(n, k, edges)
    print(result)

