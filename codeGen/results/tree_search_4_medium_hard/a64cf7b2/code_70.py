from collections import defaultdict

def solve():
    n, m, T = map(int, input().split())
    edges = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, input().split())
        edges[u].append((v, t))
    
    dp = {}
    memo = {}
    
    def dfs(u, t):
        if (u, t) in dp:
            return dp[(u, t)]
        
        if t <= 0:
            return 0
        
        if u == n:
            return 1
        
        visited = 0
        for v, w in edges[u]:
            if v != n and dfs(v, t - w) + 1 > visited:
                visited = dfs(v, t - w) + 1
        
        dp[(u, t)] = visited
        return visited
    
    path = []
    k = dfs(1, T)
    
    while k > 0:
        max_visited = 0
        next_vertex = None
        for v in range(n):
            if (v, T) not in memo:
                continue
            visited = memo[(v, T)]
            if visited > max_visited:
                max_visited = visited
                next_vertex = v
        
        path.append(next_vertex)
        k -= 1
    
    print(k)
    print(' '.join(map(str, path[::-1])))

if __name__ == "__main__":
    solve()
