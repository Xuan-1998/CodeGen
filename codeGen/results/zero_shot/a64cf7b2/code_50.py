n, m, T = map(int, input().split())
edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

graph = [[] for _ in range(n + 1)]
for u, v, t in edges:
    graph[u].append((v, t))

def dfs(vertex, remaining_time):
    if vertex > n:
        return []
    if vertex == n:
        return [vertex]
    visited = set()
    result = []
    for neighbor, time in graph[vertex]:
        if time <= remaining_time and neighbor not in visited:
            path = dfs(neighbor, remaining_time - time)
            if path:
                result.append(vertex)
                result.extend(path)
                break
    return result

result = dfs(1, T)

if not result:
    print(-1)
else:
    print(len(result))
    print(' '.join(map(str, result)))
