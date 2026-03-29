import sys

def solve():
    n, m, T = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    
    dp = [[0] * (T + 1) for _ in range(n + 1)]

    for u, v, t in edges:
        for j in range(T, t - 1, -1):
            if dp[u][j] > dp[v][j - t]:
                dp[v][j] = dp[u][j]
                break
    
    max_vertices = 0
    visited = []
    for i in range(n + 1)[::-1]:
        for j in range(T, -1, -1):
            if dp[i][j] > max_vertices:
                max_vertices = dp[i][j]
                visited = [i]
                break
        else:
            continue
        break
    
    print(max_vertices)
    print(*visited)

if __name__ == "__main__":
    solve()
