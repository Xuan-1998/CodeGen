from collections import defaultdict

def max_vertices(n, m, T):
    graph = defaultdict(list)
    dp = [[0] * (T + 1) for _ in range(n + 1)]
    
    # Build the graph and initialize dp
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))
        
    for i in range(1, n + 1):
        for j in range(T + 1):
            if not graph[i]:
                continue
            
            max_reachable = 0
            remaining_time = j
            for neighbor, edge_time in graph[i]:
                if remaining_time >= edge_time:
                    reachable_neighbors = dp[neighbor][remaining_time - edge_time] + 1
                    max_reachable = max(max_reachable, reachable_neighbors)
                
            dp[i][j] = max_reachable
    
    return dp[n][T]
