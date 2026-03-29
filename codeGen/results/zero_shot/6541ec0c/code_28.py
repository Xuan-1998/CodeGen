import sys

n = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))

graph = {}
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

connected_components = {}
visited = set()
for node in graph:
    if node not in visited:
        component = []
        dfs(node, graph, visited, component)
        connected_components[len(component)] = component

def dfs(node, graph, visited, component):
    visited.add(node)
    component.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, component)

for component in connected_components.values():
    xor_value = 0
    for node in component:
        xor_value ^= values[node-1]
    if len(connected_components) > 1 or xor_value != 0:
        print("NO")
        break
else:
    print("YES")
