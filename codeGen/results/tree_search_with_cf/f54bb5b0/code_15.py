python
import sys
input = sys.stdin.read
from collections import defaultdict

def count_pairs_with_distance_k(n, k, edges):
    # Adjacency list representation of the tree
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # dp[u][d] will store number of vertices at distance d from u
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Initialize dp[u][0] = 1 for all u
    for u in range(1, n + 1):
        dp[u][0] = 1
    
    # Result variable to store the number of pairs
    result = 0
    
    def dfs(node, parent):
        nonlocal result
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            # Count pairs where the path length is exactly k
            for d in range(1, k + 1):
                result += dp[node][d - 1] * dp[neighbor][k - d]
            # Update dp[node] using dp[neighbor]
            for d in range(1, k + 1):
                dp[node][d] += dp[neighbor][d - 1]
    
    # Start DFS from node 1 (assuming 1-indexed nodes)
    dfs(1, -1)
    
    return result

def main():
    # Read input
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
    
    # Get the result
    result = count_pairs_with_distance_k(n, k, edges)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()

