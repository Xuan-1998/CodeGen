===BEGIN CODE===
def recompute_paths(n, m, edges, p):
    has_edge = [[] for _ in range(n+1)]
    for u, v in edges:
        has_edge[u].append(v)
    
    dp = [float('inf')] * (n+1)
    dp[0] = 0

    memo = {}

    def dfs(i):
        if i == n: return 0
        if i not in memo:
            res = min(dfs(j) + 1 for j in range(p[k-1]+1, i+1) if has_edge[j][i])
            memo[i] = res
        return memo[i]

    min_recompute = float('inf')
    max_recompute = 0

    for k in range(1, len(p)):
        i, j = p[k-1], p[k]
        dp[i] = dfs(i)
        min_recompute = min(min_recompute, dp[i])
        max_recompute = max(max_recompute, dp[i])

    return min_recompute, max_recompute

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

min_recompute, max_recompute = recompute_paths(n, m, edges, p)

print(*[min_recompute, max_recompute], sep=' ')
===END CODE===
