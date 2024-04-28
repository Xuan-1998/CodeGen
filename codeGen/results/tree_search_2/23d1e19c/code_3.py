from collections import defaultdict

def dfs(v, path):
    if (v, tuple(path)) in memo:
        return memo[(v, tuple(path))]
    
    min_recomp = float('inf')
    max_recomp = 0
    for u in path:
        if u == v:
            min_recomp = 1
            max_recomp = 1
            break
        else:
            res = dfs(u, path + [v])
            min_recomp = min(min_recomp, res[0] + (1 if u in graph[v] else 0))
            max_recomp = max(max_recomp, res[1] + (1 if u in graph[v] else 0))
    
    memo[(v, tuple(path))] = (min_recomp, max_recomp)
    return (min_recomp, max_recomp)

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    k = int(input())
    path = list(map(int, input().split()))
    
    memo = {}
    dp = {(v, tuple([s])) for s in range(1, n+1)}
    
    min_recomp_all = float('inf')
    max_recomp_all = 0
    for v in range(n):
        if v not in path:
            res = dfs(v, path[:k])
            min_recomp_all = min(min_recomp_all, res[0])
            max_recomp_all = max(max_recomp_all, res[1])
    
    print(f"{min_recomp_all} {max_recomp_all}")

solve()
