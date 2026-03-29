from collections import deque

def solve():
    n = int(input())
    roads = [list(map(int, input().split())) for _ in range(n-1)]

    # Build the directed tree
    graph = [[] for _ in range(n+1)]
    for road in roads:
        graph[road[0]].append(road[1])

    # Calculate the maximum distance from the root node to each node
    max_distance = [0] * (n+1)
    queue = deque([(1, 0)])  # Start from the root node with distance 0

    while queue:
        node, distance = queue.popleft()
        for neighbor in graph[node]:
            if max_distance[neighbor] < distance + 1:
                max_distance[neighbor] = distance + 1
                queue.append((neighbor, distance + 1))

    # Find all possible ways to choose the capital
    capitals = [i for i in range(2, n+1) if max_distance[i] == min(max_distance)]

    # Print the results
    print(min(max_distance[2:]))
    print(*capitals, sep='\n')

solve()
