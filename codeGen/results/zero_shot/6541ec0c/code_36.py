import sys

n, k = map(int, sys.stdin.readline().split())
values = list(map(int, sys.stdin.readline().split()))
edges = []
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

components = {i: set() for i in range(n)}
xor_values = {}
for value in values:
    xor_values[value] = value

def dfs(node, parent):
    component = set()
    xor_value = xor_values[values[node]]
    for neighbor in [edge[1] for edge in edges if edge[0] == node]:
        if neighbor != parent:
            if values[neighbor] ^ xor_value not in xor_values:
                xor_values[values[neighbor]] = values[neighbor]
            component.update({node, neighbor})
            component.update(dfs(neighbor, node))
    return component

for i in range(n):
    components[i] = dfs(i, -1)

def is_possible():
    xor_values_set = set(xor_values.values())
    for component in components.values():
        xor_value = 0
        for node in component:
            xor_value ^= values[node]
        if xor_value not in xor_values_set:
            return False
    return True

print("YES" if is_possible() else "NO")
