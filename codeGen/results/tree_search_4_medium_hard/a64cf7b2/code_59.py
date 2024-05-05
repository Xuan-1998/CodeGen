from collections import defaultdict

def solve(n, m, T):
    edges = [(u-1, v-1, t) for u, v, t in [list(map(int, line.split())) for line in stdin.readlines()]]
    graph = defaultdict(list)
    for u, v, t in edges:
        graph[u].append((v, t))
    dp = [[0] * n for _ in range(n)]
    
    def dfs(i, prev):
        if i == 1:
            return 1
        if dp[i][prev] != -1:
            return dp[i][prev]
        
        max_vertices = 0
        for j, t in graph.get(prev, []):
            if t <= T:
                max_vertices = max(max_vertices, dfs(j, i) + 1)
        dp[i][prev] = max_vertices
        return max_vertices
    
    k = dfs(n-1, -1)
    route = []
    i = n-1
    while i > 0:
        for j, t in graph.get(i, []):
            if dfs(j, i) + 1 == k and t <= T:
                route.append(str(i+1))
                i = j
                break
    print(k)
    print(' '.join(route[::-1]))
