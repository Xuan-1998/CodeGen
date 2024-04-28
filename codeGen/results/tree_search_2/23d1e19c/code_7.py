def recomputations():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    k = int(input())
    path = list(map(int, input().split()))
    
    dp = [[0, 0] for _ in range(n+1) for _ in range(k)]
    for i in range(k-1):
        v = path[i]
        for j in range(i+1, k):
            w = path[j]
            if graph[v].count(w):
                dp[w][j] = (min(dp[v][i], 1), max(dp[v][i], 1))
    
    min_rec, max_rec = float('inf'), 0
    for i in range(k-1, -1, -1):
        v = path[i]
        rec = (dp[v][i][0] if i > 0 else 0, dp[v][i][1] if i > 0 else 0)
        min_rec = min(min_rec, rec[0])
        max_rec = max(max_rec, rec[1])
    
    print(min_rec, max_rec)

recomputations()
