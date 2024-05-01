def recomputation_times():
    n, m = map(int, input().split())
    graph = [list() for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    k = int(input())
    p = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    for i in range(k-1):
        dp[p[i+1]] = max(dp[p[i+1]], dp[p[i]] + 1)
    
    return min(dp[t], dp[p[-1]] + k - len(p) + 1)

print(recomputation_times())
