def min_max_recomputations():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    k = int(input())
    path = list(map(int, input().split()))
    
    dp_min = [0] * (n+1)
    dp_max = [0] * (n+1)
    
    for i in range(2, n+1):
        if graph[i]:
            for u in graph[i]:
                if u in path:
                    dp_min[i] = max(dp_min[i], dp_min[u])
                    dp_max[i] = min(dp_max[i], dp_max[u])
                else:
                    dp_min[i] = max(dp_min[i], dp_min[u]+1)
                    dp_max[i] = min(dp_max[i], dp_max[u]+1)
    
    return dp_min[-1], dp_max[-1]

print(*min_max_recomputations(), sep=' ')
