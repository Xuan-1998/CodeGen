from collections import defaultdict

def dfs(i, remaining_time, visited, memo):
    if (i, remaining_time) in memo:
        return memo[(i, remaining_time)]

    if i == n:  # base case: we've reached the destination vertex
        return 1, set([n])

    max_vertices = 0
    best_route = None

    for neighbor, time in graph[i]:
        if time <= remaining_time:
            new_visited = visited | {neighbor}
            new_remaining_time = remaining_time - time
            vertices, route = dfs(neighbor, new_remaining_time, new_visited, memo)
            if vertices + 1 > max_vertices and time + sum(graph[neighbor]) <= T:
                max_vertices = vertices + 1
                best_route = route | {i}

    memo[(i, remaining_time)] = max_vertices, best_route
    return max_vertices, best_route

n, m, T = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v, time = map(int, input().split())
    graph[u].append((v, time))

max_vertices, route = dfs(1, T, set(), {})
print(max_vertices)
print(*route, sep='\n')
