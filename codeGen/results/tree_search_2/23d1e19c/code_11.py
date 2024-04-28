from collections import defaultdict

def min_max_recomputations(n, m, edges, k, path):
    dp = [[float('inf'), 0] for _ in range(n+1)]
    dp[0][0] = 0
    
    d = defaultdict(int)
    
    for i in range(k-1):
        u, v = path[i], path[i+1]
        if (u, v) not in edges:
            continue
        if i == 0:
            min_recomputations = 0
        else:
            min_recomputations = dp[path[i]][1] + 1
        max_recomputations = min_recomputations
        for j in range(n+1):
            if (j, v) not in edges and d.get(j) == 0:
                dp[j][0] = min(dp[j][0], dp[v][0] + 1)
                dp[j][1] = max(dp[j][1], dp[v][1] + 1)
    
    return [dp[-1][0], dp[-1][1]]

n, m = map(int, input().split())
edges = [(u-1, v-1) for u, v in (map(int, line.split()) for line in range(m))]
k = int(input())
path = [int(x)-1 for x in input().split()]

print(*min_max_recomputations(n, m, edges, k, path))
