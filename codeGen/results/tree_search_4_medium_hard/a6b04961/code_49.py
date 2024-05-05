from collections import defaultdict

def dp(u, v):
    memo = defaultdict(int)
    def dfs(t, s):
        if (t, s) in memo:
            return memo[(t, s)]
        if t == 0 or s == m:
            return 0
        res = max(dfs(min(t-1, s), 0)*max(t-1,s) + t*s,
                  dfs(t-1, s+1)*t*s)
        memo[(t, s)] = res
        return res

    n, m = map(int, input().split())
    for _ in range(m):
        u, v = map(int, input().split())
        # Add the edge to the graph if necessary
        pass
    print(dfs(n, 0))
