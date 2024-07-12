python
import sys
from collections import defaultdict

sys.setrecursionlimit(200000)

def count_pairs(n, k, edges):
    # Build the tree
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    result = 0

    def dfs(node, parent):
        nonlocal result
        # dp[i] will be the number of paths of length i ending at this node
        dp = [0] * (k + 1)
        dp[0] = 1  # There's always one way to be at the current node with path length 0
        
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            child_dp = dfs(neighbor, node)
            
            # Calculate the number of pairs with path length k
            for i in range(k):
                result += dp[i] * child_dp[k - i - 1]
            
            # Update dp array for the current node
            for i in range(k):
                dp[i + 1] += child_dp[i]
        
        return dp
    
    dfs(1, -1)
    return result

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    edges = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(n - 1)]
    print(count_pairs(n, k, edges))

