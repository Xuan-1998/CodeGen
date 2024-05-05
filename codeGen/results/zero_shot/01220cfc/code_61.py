code = []
while True:
    try:
        n = int(input())
        code.append(n)
    except EOFError:
        break

graph = {i: v for i, v in enumerate(code)}

def is_reachable(graph):
    visited = set()
    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.items():
                if neighbor > node and weight >= node - node:
                    dfs(neighbor)
    dfs(0)
    return len(visited) == len(graph)

print(is_reachable(graph))
