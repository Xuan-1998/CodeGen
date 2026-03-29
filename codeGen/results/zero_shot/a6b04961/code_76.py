import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        if u != v:  # ignore self-loops
            edges.append((u, v))
    return n, edges

def build_graph(n, edges):
    graph = {i: [] for i in range(1, n+1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # assume undirected graph
    return graph

def find_simple_paths(graph):
    visited = [False] * (n + 1)
    simple_paths = []
    for i in range(1, n+1):  # start from each vertex
        if not visited[i]:
            stack = [(i, [i])]
            while stack:
                node, path = stack.pop()
                if len(path) > 2:  # avoid single vertices and edges
                    simple_paths.append(path)
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append((neighbor, path + [neighbor]))
    return simple_paths

def check_tail(path):
    is_tail = True
    for i in range(1, len(path)):
        if path[i-1] not in graph[path[i]]:
            is_tail = False
            break
    return is_tail

def calculate_beauty(tail):
    spine_count = 0
    for edge in edges:
        if tail[0] == edge[0] and edge[1] not in tail:
            spine_count += 1
        elif tail[-1] == edge[1] and edge[0] not in tail:
            spine_count += 1
    return len(tail) * spine_count

def find_max_beauty(simple_paths):
    max_beauty = 0
    for path in simple_paths:
        if check_tail(path):
            beauty = calculate_beauty(path)
            max_beauty = max(max_beauty, beauty)
    return max_beauty

n, edges = read_input()
graph = build_graph(n, edges)
simple_paths = find_simple_paths(graph)
max_beauty = find_max_beauty(simple_paths)

print(max_beauty)
