from collections import defaultdict

def max_vertices(n, m, T):
    edges = [(u, v, t) for _ in range(m)]
    
    dp = [[0] * (T + 1) for _ in range(n + 1)]
    memo = defaultdict(dict)
    
    def dfs(i, v):
        if i == n:
            return v + 1
        if (i, v) in memo:
            return memo[(i, v)]
        
        max_vertices = 0
        for u, v_edge, t_edge in edges:
            if t_edge <= v:
                temp_v = v - t_edge
                max_vertices = max(max_vertices, dfs(u, temp_v))
        dp[i][v] = max_vertices + (1 if i == n else 0)
        
        memo[(i, v)] = dp[i][v]
        return dp[i][v]
    
    k = dfs(1, T)
    visited = []
    current_vertex = n
    remaining_time = k - 1
    
    while current_vertex > 0:
        for u, v_edge, t_edge in edges:
            if t_edge <= remaining_time and u == current_vertex:
                visited.append(current_vertex)
                current_vertex = v_edge
                remaining_time -= t_edge
                break
        if not (current_vertex, remaining_time) in memo:
            k = dfs(1, T - remaining_time)
    
    return k, ' '.join(map(str, visited[::-1]))
