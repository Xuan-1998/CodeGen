def min_max_recomputations():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    s, t, k = map(int, input().split())
    path = list(map(int, input().split()))
    path_dict = {i: p for i, p in zip(path, range(1, len(path)+1))}
    
    dp = [[0, 0] for _ in range(n+1)]
    for v in range(1, n+1):
        if v == t:
            dp[v] = [0, 0]
        else:
            for u in graph[v]:
                dp[v][0] = min(dp[u][0], dp[v][0]) + 1
                dp[v][1] = max(dp[u][1], dp[v][1])
    
    print(*dp[t])

if __name__ == "__main__":
    min_max_recomputations()
