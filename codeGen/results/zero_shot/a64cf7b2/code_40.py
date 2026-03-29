import sys
from collections import defaultdict

def solve():
    n, m, T = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))
        
    visited = [False] * (n + 1)
    dp = [[0, []] for _ in range(n + 1)]
    dp[1][0] = T
    
    for i in range(2, n + 1):
        max_time = 0
        route = []
        
        for j in graph[i]:
            if not visited[j[0]]:
                time, prev_route = dp[j[0]]
                
                if time <= T - j[1] and time + j[1] > max_time:
                    max_time = time + j[1]
                    route = prev_route + [i]
                    
        visited[i] = True
        dp[i][0] = max_time
        dp[i][1] = route
        
    k = 0
    for i in range(2, n + 1):
        if dp[i][0] > 0:
            print(i)
            k += 1
    
    for i in range(k):
        print(dp[k - i - 1][1][-1])
