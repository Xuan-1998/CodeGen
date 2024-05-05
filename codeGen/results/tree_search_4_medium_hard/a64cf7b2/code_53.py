from collections import defaultdict

def dp_time_limit(n, m, T):
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))
    
    memo = [[0] * (T + 1) for _ in range(n + 1)]
    
    def dfs(i, j):
        if i == n:
            return 1
        if memo[i][j]:
            return memo[i][j]
        
        max_time = 0
        visited = 0
        
        for v, t in graph[i]:
            time = min(j, T) - t
            visited += dfs(v, time)
            max_time = max(max_time, time + 1)
        
        memo[i][j] = visited + (max_time == j)
        return memo[i][j]
    
    print(dfs(1, T))
    path = []
    
    i, j = n, T
    while i != 1:
        for v, t in graph[i]:
            if min(j, T) - t > 0:
                j -= max(j, T) - t
                path.append(v)
                break
        i = v
    
    print(*reversed(path), sep='\n')

if __name__ == "__main__":
    n, m, T = map(int, input().split())
    dp_time_limit(n, m, T)
