from collections import deque

def minmax_recomputations():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    k = int(input())
    path = list(map(int, input().split()))
    
    # Initialize dynamic programming arrays
    dp = [[0, 0] for _ in range(n + 1)]
    
    # Fill dynamic programming arrays
    queue = deque([(path[0], 0)])
    while queue:
        vertex, recomputations = queue.popleft()
        if vertex != path[k - 1]:
            for neighbor in graph[vertex]:
                if neighbor not in [p for p in path[:k]]:
                    queue.append((neighbor, recomputations + 1))
        else:
            dp[path[k - 1]][0] = recomputations
            dp[path[k - 1]][1] = recomputations
    
    # Compute minimum and maximum number of recomputations needed
    min_recomputations = max(dp[i][0] for i in range(1, n + 1))
    max_recomputations = max(dp[i][1] for i in range(1, n + 1))
    
    print(min_recomputations, max_recomputations)

minmax_recomputations()
