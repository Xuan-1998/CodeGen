import heapq

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        edges = [(int(u), int(v)) for _ in range(n-1)]
        m = int(input())
        prime_factors = [int(x) for x in input().split()]
        
        # Initialize memoization table
        dp = [0] * (n + 1)
        max_dp = 0
        
        def dfs(u):
            nonlocal max_dp
            if dp[u]: return dp[u]
            
            # Calculate edge labels
            edge_labels = 1
            for _, v in edges:
                if u == v: continue
                edge_labels *= (v - u)
            
            # Update memoization table and maximum value
            dp[u] = product(edge_labels, dfs(v) if len(edges) > 0 else 1)
            max_dp = max(max_dp, dp[u])
            return dp[u]
        
        root = 1
        for _ in range(n-1):
            u, v = next(edges)
            if u == root:
                root = v
        dfs(root)
        
        print((max_dp % (10**9 + 7)))
