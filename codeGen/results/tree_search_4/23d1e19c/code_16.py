from collections import defaultdict

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
path = list(map(int, input().split()))

dp_tabulation = [[0] * (n + 1) for _ in range(k + 1)]

graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)

def edge_exists(i, k):
    return k in graph[i]

for i in range(1, k + 1):
    for j in range(1, n + 1):
        if j == path[i - 1]:
            dp_tabulation[i][j] = dp_tabulation[i - 1][path[i - 2]] + 1
        else:
            dp_tabulation[i][j] = max(dp_tabulation[i - 1][k] + 1 for k in range(1, n + 1) if edge_exists(i, k) and k != j)

min_recomputation = min([dp_tabulation[k - 1][path[-1]] for k in range(2, k + 1)])
max_recomputation = max([dp_tabulation[k - 1][path[-1]] for k in range(2, k + 1)])

print(min_recomputation, max_recomputation)
