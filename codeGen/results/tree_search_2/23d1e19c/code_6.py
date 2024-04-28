from collections import defaultdict

def dp_recomputation(graph, fixed_path):
    n = len(graph)
    memo = {}

    def dfs(v, prev_path):
        if (v, tuple(prev_path)) in memo:
            return memo[(v, tuple(prev_path))]
        
        if v == t:
            return 0, 0

        min_recomputation = float('inf')
        max_recomputation = -float('inf')

        for next_v in graph[v]:
            if next_v not in prev_path and next_v != s:  # skip the initial vertex
                rec_min, rec_max = dfs(next_v, prev_path + [next_v])
                min_recomputation = min(min_recomputation, rec_min + (1 if v != fixed_path[i-1] else 0))
                max_recomputation = max(max_recomputation, rec_max + (1 if v != fixed_path[i-1] else 0))
        
        memo[(v, tuple(prev_path))] = min_recomputation, max_recomputation
        return min_recomputation, max_recomputation

    s, t = fixed_path[0], fixed_path[-1]
    min_recomputation, max_recomputation = dfs(s, [])
    
    return min_recomputation, max_recomputation


n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
fixed_path = list(map(int, input().split()))

min_rec, max_rec = dp_recomputation(graph, fixed_path)
print(*[min_rec, max_rec], sep=' ')
