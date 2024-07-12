python
import sys
input = sys.stdin.read
from collections import defaultdict, deque

def count_pairs(n, k, edges):
    # Build the adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # DP array to store number of nodes at each depth
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = [0]

    def dfs(node, parent):
        dp[node][0] = 1  # There's always one way to be at depth 0 (the node itself)
        
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            
            # Count pairs with paths of length k
            for i in range(k):
                result[0] += dp[node][i] * dp[neighbor][k - i - 1]
            
            # Merge dp[neighbor] into dp[node]
            for i in range(1, k + 1):
                dp[node][i] += dp[neighbor][i - 1]
    
    dfs(1, -1)
    return result[0]

if __name__ == "__main__":
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    edges = []
    index = 2
    for _ in range(n - 1):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2
    
    print(count_pairs(n, k, edges))

