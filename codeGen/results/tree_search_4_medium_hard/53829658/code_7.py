def dfs(graph, parent, dp):
    n = len(graph)
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            dfs_helper(graph, i, parent, visited, dp)

def dfs_helper(graph, city, parent, visited, dp):
    n = len(graph)
    if visited[city]:
        return

    visited[city] = True

    min_distance = float('inf')
    for neighbor in graph[city]:
        if neighbor == parent:
            continue
        if not visited[neighbor]:
            dfs_helper(graph, neighbor, city, visited, dp)
        else:
            distance = dp[neighbor]
        if distance < min_distance:
            min_distance = distance

    dp[city] = min_distance + 1

def find_optimal_capital(graph):
    n = len(graph)
    parent = -1
    dp = [float('inf')] * n

    for i in range(n-1):
        u, v = map(int, input().split())
        graph[v-1].append(u-1)

    dfs(graph, parent, dp)

    min_distance = max(dp)
    optimal_capital = dp.index(min_distance) + 1
    return min_distance, optimal_capital

if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n)]
    min_distance, optimal_capital = find_optimal_capital(graph)

    print(min_distance)
    path = [optimal_capital]
    while len(path) < n:
        parent = -1
        max_distance = 0
        for i in reversed(range(len(path))):
            for neighbor in graph[path[i]]:
                if neighbor not in path and dp[neighbor] > max_distance:
                    parent = neighbor
                    max_distance = dp[neighbor]
        path.append(parent)
    print(*path[::-1], sep=' ')
