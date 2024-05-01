import sys

def compute_recomputations():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    s, t, k = map(int, input().split())
    path = list(map(int, input().split()))
    
    dp = [[(0, 0) for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][t] = (0, 0)
    
    for u, v in edges:
        for p in path:
            if u == p and v in {p-1, p}:
                dp[u][v] = min(dp[u][p] + (1, 1), (1, 1))
    
    for i in range(n+1):
        print(*dp[s][i], sep=' ')

compute_recomputations()
