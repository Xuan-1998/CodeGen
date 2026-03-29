import sys

def solve(n, m, T):
    memo = {}

    def dfs(i, t):
        if (i, t) in memo:
            return memo[(i, t)]
        
        max_visited = 0
        for j, w in edges:
            if i == j or w > t:
                continue
            visited = dfs(j, t-w)
            if visited + 1 > max_visited:
                max_visited = visited + 1
        
        memo[(i, t)] = max_visited
        return max_visited

    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    edges.sort(key=lambda x: x[2])

    max_visited = dfs(n, T)
    visited_vertices = [i for i in range(1, n+1) if dfs(i, T) == max_visited]

    print(max_visited)
    print(*visited_vertices, sep='\n')
