import sys
input = sys.stdin.read
from collections import defaultdict

def count_pairs_with_path_length_k(n, k, edges):
    # Build the adjacency list
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # Initialize the dp table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # DFS function to fill the dp table
    def dfs(node, parent):
        dp[node][0] = 1
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            for d in range(1, k + 1):
                dp[node][d] += dp[neighbor][d - 1]
    
    # Perform DFS starting from node 1 (assuming 1-based indexing)
    dfs(1, -1)
    
    # Count the number of valid pairs
    result = 0
    
    def count_pairs(node, parent):
        nonlocal result
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            # Count pairs where the path goes through the current node
            for d in range(1, k):
                result += dp[neighbor][d - 1] * (dp[node][k - d] - dp[neighbor][k - d - 1])
            count_pairs(neighbor, node)
    
    count_pairs(1, -1)
    
    # Since each pair is counted twice, divide the result by 2
    return result // 2

def main():
    data = input().strip().split()
    n = int(data[0])
    k = int(data[1])
    edges = []
    for i in range(2, len(data), 2):
        a = int(data[i])
        b = int(data[i + 1])
        edges.append((a, b))
    
    result = count_pairs_with_path_length_k(n, k, edges)
    print(result)

if __name__ == "__main__":
    main()

