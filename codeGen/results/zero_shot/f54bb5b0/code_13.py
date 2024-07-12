python
import sys
from collections import defaultdict, deque

def count_pairs_with_path_length_k(n, k, edges):
    # Adjacency list for the tree
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # To store the result
    result = 0
    
    # Function to perform DFS and count paths
    def dfs(node, parent):
        nonlocal result
        # dp[i] will store the number of nodes at distance i from the current node
        dp = [0] * (k + 1)
        dp[0] = 1  # The distance from the node to itself is 0
        
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            child_dp = dfs(neighbor, node)
            # Count pairs between current node and its subtree
            for i in range(k):
                result += dp[i] * child_dp[k - i - 1]
            # Merge the child_dp into dp
            for i in range(k):
                dp[i + 1] += child_dp[i]
        
        return dp
    
    # Start DFS from node 1 (assuming nodes are 1-indexed)
    dfs(1, -1)
    
    return result

def main():
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

if __name__ == "__main__":
    main()

