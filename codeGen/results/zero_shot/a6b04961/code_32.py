import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph.append((u, v))

adj_list = {i: [] for i in range(n)}
for u, v in graph:
    adj_list[u].append(v)
    adj_list[v].append(u)

def dfs(node, visited, path_length):
    global max_tail_length, max_tail
    if len(visited) > max_tail_length:
        max_tail_length = len(visited)
        max_tail = list(visited)
    for neighbor in adj_list[node]:
        if neighbor not in visited:
            dfs(neighbor, visited + [node], path_length + 1)

max_tail_length = 0
max_tail = []
for i in range(n):
    dfs(i, [i], 1)

print(max_tail_length)

def is_spine(edge):
    u, v = edge
    return max_tail.index(u) < max_tail.index(v)

spine_count = sum(1 for _ in filter(is_spine, graph))

print(max_tail_length * spine_count)
