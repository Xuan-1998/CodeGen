dp = {}
def dp(i, t):
    if (i, t) in memo:
        return memo[(i, t)]
    
    if i == n:
        return 1
    
    res = 0
    for j in range(m):
        if graph[j][0] == i and graph[j][2] <= t:
            res = max(res, dp(graph[j][1], t - graph[j][2]) + 1)
    
    memo[(i, t)] = res
    return res

n, m, T = map(int, input().split())
graph = []
for _ in range(m):
    u, v, t = map(int, input().split())
    graph.append((u, v, t))

res = 0
curr_t = T
for i in range(n-1, -1, -1):
    res = max(res, dp(i, curr_t))
    curr_t -= min(curr_t, [x[2] for x in graph if x[0] == i][0]) if any(x[0] == i for x in graph) else 0
    
print(res)
for _ in range(res):
    i = n-1
    while True:
        for j in range(m):
            if graph[j][0] == i and [x[2] for x in graph if x[0] == i][0] <= curr_t:
                i, curr_t = graph[j][1], curr_t - graph[j][2]
                break
        else:
            print(i)
            res -= 1
            break
