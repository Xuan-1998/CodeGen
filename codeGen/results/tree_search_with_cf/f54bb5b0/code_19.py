import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000)

def solve():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    
    edges = []
    index = 2
    for _ in range(n - 1):
        a = int(data[index]) - 1
        b = int(data[index + 1]) - 1
        edges.append((a, b))
        index += 2
    
    # Build the tree as an adjacency list
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # dp[u][d] = number of vertices at distance d from u
    dp = [[0] * (k + 1) for _ in range(n)]
    
    def dfs(u, parent):
        dp[u][0] = 1
        
        for v in tree[u]:
            if v == parent:
                continue
            dfs(v, u)
            # Combine dp values from child v into dp[u]
            for d in range(1, k + 1):
                dp[u][d] += dp[v][d - 1]
    
    # Perform DFS from an arbitrary root (say node 0)
    dfs(0, -1)
    
    # Count the number of pairs with distance exactly k
    result = 0
    
    def count_pairs(u, parent):
        nonlocal result
        
        # For each child v of u, count pairs (u, v) with path length k passing through u
        for v in tree[u]:
            if v == parent:
                continue
            
            # For each d from 1 to k-1, count pairs with distance exactly k
            for d in range(1, k):
                result += dp[v][d - 1] * (dp[u][k - d] - dp[v][k - d - 1])
            
            # Recursively count pairs in the subtree rooted at v
            count_pairs(v, u)
    
    count_pairs(0, -1)
    
    # Each pair is counted twice, so divide the result by 2
    print(result // 2)


