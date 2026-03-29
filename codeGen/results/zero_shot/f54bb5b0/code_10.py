import sys
input = sys.stdin.read
from collections import defaultdict, deque

def count_paths_of_length_k(n, k, edges):
    if k == 0:
        return n  # Each vertex is a path of length 0 with itself
    
    # Build the adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # DP table to store the number of paths of length i ending at vertex v
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # To store the total number of paths of length k
    result = 0
    
    def dfs(v, parent):
        nonlocal result
        dp[v][0] = 1  # There's one path of length 0 ending at v (the vertex itself)
        
        for neighbor in adj[v]:
            if neighbor == parent:
                continue
            dfs(neighbor, v)
            for i in range(1, k + 1):
                result += dp[v][i - 1] * dp[neighbor][k - i]
            for i in range(1, k + 1):
                dp[v][i] += dp[neighbor][i - 1]
    
    dfs(1, -1)
    return result

def main():
    data = input().strip().split()
    n = int(data[0])
    k = int(data[1])
    edges = []
    index = 2
    for _ in range(n - 1):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2
    
    result = count_paths_of_length_k(n, k, edges)
    print(result)

if __name__ == "__main__":
    main()

