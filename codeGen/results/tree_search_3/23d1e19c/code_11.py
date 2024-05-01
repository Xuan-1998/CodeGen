import sys

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    fixed_path = list(map(int, input().split()))
    memo = {i: [float('inf'), 0] for i in range(1, n+1)}
    
    def dfs(i, k):
        if k > len(fixed_path) or i != fixed_path[k-1]:
            return float('inf'), 1
        if memo[i][0] <= k:
            return memo[i]
        
        res = [float('inf'), 0]
        for j in range(i):
            if graph[j].count(i):
                dp, dpr = dfs(j, k)
                if dp + 1 < res[0]:
                    res[0] = dp + 1
                    res[1] = min(res[1], dpr) + 1
        
        memo[i] = res
        return res
    
    res = [float('inf'), 0]
    for i in range(1, n+1):
        r, c = dfs(i, len(fixed_path))
        if r < res[0]:
            res[0], res[1] = r, min(res[1], c)
    
    print(*res)

solve()
