import heapq

def min_max_recomputations(graph, fixed_path):
    n = len(graph)
    dp = [[float('inf'), 0] for _ in range(n)]
    queue = [(0, fixed_path[0])]

    for j in range(len(fixed_path) - 1):
        while queue:
            dist, vertex = heapq.heappop(queue)

            if dp[vertex][j][0] < float('inf'):
                continue

            if j > 0:
                dp_vertex = min_max_recomputations_helper(graph, fixed_path[:j + 1], vertex)
                dp[vertex][j] = [dp_vertex[0], max(dp_vertex[1], j)]
            else:
                dp[vertex][j] = [1, j]

            for neighbor in range(n):
                if graph[vertex][neighbor]:
                    heapq.heappush(queue, (dist + 1, neighbor))

    min_recomputations = float('inf')
    max_recomputations = 0

    for vertex in range(1, n):
        min_recomputations = min(min_recomputations, dp[vertex][-1][0])
        max_recomputations = max(max_recomputations, dp[vertex][-1][1])

    return [min_recomputations, max_recomputations]

def min_max_recomputations_helper(graph, path, vertex):
    n = len(graph)
    if vertex == path[-1]:
        return 1, 0

    dp_vertex = float('inf'), 0
    for neighbor in range(n):
        if graph[path[-1]][neighbor] and neighbor not in path:
            dist, _ = min_max_recomputations_helper(graph, path + [neighbor], neighbor)
            dp_vertex = min((dp_vertex[0], dp_vertex[1]), (dist, j))
            break

    return *dp_vertex

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[False] * n for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1][v - 1] = True
    k = int(input())
    fixed_path = [int(x) - 1 for x in input().split()]

    result = min_max_recomputations(graph, fixed_path)
    print(*result)

