n, *w = map(int, input().split())
graph = {}
for i, (u, v, c) in enumerate([map(int, line.split()) for line in stdin]):
    graph[u] = {'child': v, 'length': c}
parent = {}

def build_tree(node):
    if node not in graph:
        return
    child = graph[node]['child']
    length = graph[node]['length']
    parent[node] = None
    for neighbor in [child]:
        if neighbor not in parent:
            parent[neighbor] = node
        build_tree(neighbor)

def dfs(node, target):
    if node == target:
        return w[node]
    gas = w[node] - graph[node]['length']
    for neighbor in [graph[node]['child']]:
        if neighbor not in parent or neighbor == target:
            continue
        gas += dfs(neighbor, target)
    return min(gas, target)

build_tree(1)  # assuming the root city is 1

print(dfs(1, n))
