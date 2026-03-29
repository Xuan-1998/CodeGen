import sys
from collections import defaultdict

def solve():
    n, m, T = map(int, input().split())
    
    graph = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))
    
    dp = [[0] * (T + 1) for _ in range(n + 1)]
    
    visited = set()
    def dfs(v, t):
        if v == n and t <= T:
            return 1
        if (v, t) in visited:
            return dp[v][t]
        
        visited.add((v, t))
        max_visit = 0
        for neighbor, time in graph.get(v, []):
            remaining_time = min(t - time, T)
            max_visit = max(max_visit, dfs(neighbor, remaining_time) + (t >= T))
        
        dp[v][t] = max_visit
        visited.remove((v, t))
        return dp[v][t]
    
    k = 0
    for i in range(T, -1, -1):
        if dp[n][i] > k:
            k = dp[n][i]
            break
    
    for _ in range(k):
        max_visit = 0
        v = n
        t = T
        while True:
            for neighbor, time in graph.get(v, []):
                remaining_time = min(t - time, T)
                if dp[neighbor][remaining_time] > max_visit:
                    max_visit = dp[neighbor][remaining_time]
                    v = neighbor
                    t = remaining_time
            if k == _ + 1:
                print(v, end=' ')
                break

if __name__ == "__main__":
    solve()
