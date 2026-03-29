import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)

capital = 1
min_edges = 0

for i in range(2, n + 1):
    if len(graph[i]) > 0:
        parent = i
        while True:
            parent = min((graph[parent][i], i) for i in graph[parent] if i != parent)
            if parent == capital:
                break
            min_edges += 1

print(min_edges)
print(*range(1, n + 1), sep=' ')
