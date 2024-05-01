import sys

input = lambda: [int(x) for x in input().split()]
n, m = input()
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = input()
    graph[u].append(v)
s, t, k = input()
path = list(input())
dp_min = [-1] * (n + 1)
dp_max = [0] * (n + 1)

def follow_recommendation(i):
    for j in range(len(path) - 1):
        if path[j] == i and path[j+1] == v:
            return True
    return False

def next_vertex(i):
    for v in graph[i]:
        if v == path[0]:
            return v

for i in range(1, k + 1):
    dp_min[path[i-1]] = dp_max[path[i-2]]
    dp_max[path[i-1]] = min(dp_max[v] + 1 for v in next_vertices(path[i-1])) if not follow_recommendation(path[i-1]) else dp_max[next_vertex(path[i-1])]
print(dp_min[t], dp_max[t])
