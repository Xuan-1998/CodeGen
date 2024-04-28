def solve():
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
    
    k = int(input())
    path = list(map(int, input().split()))
    
    dp = {}
    for i in range(k-1):
        v = path[i]
        prev_path = tuple(path[:i+1])
        if (v, prev_path) not in dp:
            dp[(v, prev_path)] = [float('inf'), 0] # min and max recomputations
        if v in graph:
            for neighbor in graph[v]:
                if neighbor == path[i+1]:
                    dp[(neighbor, prev_path)] = [min(dp[(v, prev_path)][0]+1, dp[(neighbor, prev_path)][0]), max(dp[(v, prev_path)][1], 1)]
    
    min_recomps, max_recomps = float('inf'), 0
    for (v, _) in dp:
        min_recomps = min(min_recomps, dp[(v,_)][0])
        max_recomps = max(max_recomps, dp[(v,_)][1])
    
    print(min_recomps, max_recomps)

if __name__ == "__main__":
    solve()
