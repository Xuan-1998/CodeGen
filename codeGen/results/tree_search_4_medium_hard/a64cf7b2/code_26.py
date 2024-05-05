import sys
from collections import defaultdict

def main():
    n, m, T = map(int, input().split())
    
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))
        
    dp = [[0] * (T + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(T + 1):
            if j < graph[i][0][1]:
                dp[i][j] = dp[i - 1][j]
            else:
                visited = set()
                current_time = 0
                max_vertices = 0
                
                for v, w in graph[i]:
                    if v not in visited and current_time + w <= j:
                        visited.add(v)
                        current_time += w
                        max_vertices = max(max_vertices, dp[v][j - w] + 1)
                        
                dp[i][j] = max_vertices
    
    k = dp[n][T]
    
    visited = set()
    current_time = 0
    vertices = []
    
    for i in range(1, n + 1):
        for v, w in graph[i]:
            if v not in visited and current_time + w <= T:
                visited.add(v)
                current_time += w
                vertices.append(i)
                
    print(k)
    print(*vertices)

if __name__ == "__main__":
    main()
