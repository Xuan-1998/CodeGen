from collections import defaultdict

def read_graph():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    return n, graph

def dfs(graph, path, used_edges, memo):
    if len(path) > 1 and (path[-2], path[-1]) in used_edges:
        return 0
    if len(path) == 1 or (len(path) > 1 and path[-1] not in [u for u, v in graph.items()]):
        if len(path) > 1:
            memo[(0, tuple(path))] = len(path)
        return len(path)

    max_beauty = 0
    for i in range(len(path)):
        for j in range(i + 1, len(path)):
            if path[i] not in [u for u, v in graph.items()] or (path[i], path[j]) in used_edges:
                continue
            new_path = list(path[:i])
            new_path.append(path[j])
            beauty = dfs(graph, new_path, used_edges | {(path[k], path[k + 1]) for k in range(i - 1, j)}, memo)
            if beauty > max_beauty:
                max_beauty = beauty
    return max_beauty

n, graph = read_graph()
memo = {}
print(dfs(graph, [0], set(), memo))
