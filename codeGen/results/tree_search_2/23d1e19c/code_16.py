def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    s, t, k = map(int, input().split())
    path = list(map(int, input().split()))
    
    dp = [[[0, 0] for _ in range(k+1)] for _ in range(n+1)]
    
    # Initialize the base case
    dp[t][0][0] = [0, 0]
    
    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            if i == path[j-1]:
                dp[i][j][0] = dp[path[j-2]][j-1][0][:]
                dp[i][j][1] = dp[path[j-2]][j-1][1][:]
            else:
                min_count = float('inf')
                max_count = 0
                for neighbor in graph[i]:
                    if neighbor == path[j-1]:
                        continue
                    new_min_count, new_max_count = dp[neighbor][j-1]
                    min_count = min(min_count, new_min_count+1)
                    max_count = max(max_count, new_max_count+1)
                dp[i][j] = [min_count, max_count]
    
    # Find the minimum and maximum number of recomputations for vertex s
    min_recomputation = dp[s][k-1][0][:]
    max_recomputation = dp[s][k-1][1][:]
    
    print(min_recomputation[0], max_recomputation[1])
