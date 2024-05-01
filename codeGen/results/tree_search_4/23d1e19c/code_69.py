from collections import deque

def min_max_recomputations(n, m, edges, k, fixed_path):
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
    
    # Memoize the shortest path computation using BFS
    memo = {}
    def shortest_path(u):
        if u not in memo:
            queue = deque([(u, 0)])  # (vertex, distance)
            while queue:
                vertex, dist = queue.popleft()
                for neighbor in graph[vertex]:
                    if neighbor == fixed_path[1]:  # t
                        return dist + 1
                    if neighbor not in memo:
                        memo[neighbor] = dist + 1
                        queue.append((neighbor, dist+1))
        return float('inf')  # if no path to t

    dp_min = [0] * (n+1)
    dp_max = [0] * (n+1)

    for i in range(k-1):
        vertex = fixed_path[i]
        next_vertex = fixed_path[i+1]
        
        # Update minimum and maximum recomputations
        dp_min[next_vertex] = min(dp_min[next_vertex], dp_min[vertex])
        dp_max[next_vertex] = max(dp_max[next_vertex], dp_max[vertex])

        # Compute the number of times shortest path needs to be recomputed
        num_recomputations = min(shortest_path(vertex), len(graph[fixed_path[i+1]])) - 1
        
        # Update minimum and maximum recomputations
        dp_min[next_vertex] += num_recomputations
        dp_max[next_vertex] += num_recomputations

    return dp_min[0], dp_max[0]

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
fixed_path = list(map(int, input().split()))

min_recomputations, max_recomputations = min_max_recomputations(n, m, edges, k, fixed_path)

print(min_recomputations, max_recomputations)
