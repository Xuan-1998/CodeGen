from collections import defaultdict

n, m, T = map(int, input().split())
edges = [(u, v, t) for u, v, t in [map(int, line.split()) for line in [input() for _ in range(m)]]]

dp = [[0] * (T + 1) for _ in range(n + 1)]
memo = defaultdict(list)

def state_transition(i, t):
    max_vertices = 0
    next_vertex = None
    for u, v, t_u in edges:
        if u < i and t >= t_u:
            new_t = t - t_u
            if dp[v][new_t] > max_vertices:
                max_vertices = dp[v][new_t]
                next_vertex = v
    return max_vertices, next_vertex

for i in range(1, n + 1):
    for t in range(T, -1, -1):
        max_vertices, next_vertex = state_transition(i, t)
        if max_vertices > dp[i][t]:
            dp[i][t] = max_vertices
            memo[(i, t)].extend(memo.get((next_vertex, new_t), [next_vertex]) for new_t in range(t - t_u, 0))

k = dp[n][T]
result = []

for i in range(n, -1, -1):
    t = T
    while dp[i][t] == k:
        result.append(i)
        t -= edges[edges.index((u, v))][2]
        i = v

print(k)
print(*reversed(result))
