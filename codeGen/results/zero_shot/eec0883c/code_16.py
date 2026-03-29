import sys

n = int(sys.stdin.readline())
w = [int(x) for x in sys.stdin.readline().split()]
graph = {}

for _ in range(n - 1):
    u, v, c = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, c))
    graph[v].append((u, c))

def dfs(node, gas_left):
    if node == 2:  # Target city reached
        return gas_left
    for neighbor, c in graph[node]:
        new_gas = min(w[neighbor], gas_left - c)
        if new_gas > 0:
            result = max(result, dfs(neighbor, new_gas))
    return result

result = 0
for node in graph:
    w_node = w[node]
    if w_node > 0:  # City has gasoline
        result = max(result, dfs(node, w_node))

print(result)
