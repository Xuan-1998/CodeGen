from collections import defaultdict

def max_vertices(graph):
    n, m, T = map(int, input().split())
    
    # Create a dictionary to store the edges and their weights
    edges = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, input().split())
        edges[u].append((v, t))
    
    # Create a memoization table to store the maximum number of vertices that can be visited
    dp = [[0] * (T + 1) for _ in range(n + 1)]
    
    def dfs(i, time):
        if dp[i][time]:
            return dp[i][time]
        
        max_visits = 0
        for j, t_edge in edges.get(i, []):
            if time - t_edge >= 0:
                for k in memoized_dict.get(j, set()):
                    if time - t_edge >= memoized_dict[k] and not visited[k]:
                        visited[k] = True
                        dp[j][time - t_edge] = max(dp[j][time - t_edge], dfs(k, time - t_edge) + 1)
                        max_visits = max(max_visits, dp[j][time - t_edge])
        
        return max_visits
    
    memoized_dict = {}
    visited = [False] * (n + 1)
    
    # Initialize the table and start the DFS from vertex 1
    dp[1][T] = 1
    max_visits = dfs(1, T)
    
    print(max_visits)
    route = []
    time_left = T
    for i in range(n - 1, -1, -1):
        while time_left > 0 and edges[i]:
            next_vertex, t_edge = min((j, t) for j, t in edges[i]), float('inf')
            if time_left >= t_edge:
                route.append(i)
                time_left -= t_edge
                break
        if i == 1:
            break
    print(*route[::-1], sep='\n')

max_vertices(input())
