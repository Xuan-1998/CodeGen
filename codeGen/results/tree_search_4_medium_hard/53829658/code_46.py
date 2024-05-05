from collections import defaultdict, deque

def invert Roads(n, roads):
    # Create an adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)

    # Initialize distances and visited sets
    dist = {i: float('inf') for i in range(1, n+1)}
    visited = set()

    def dfs(u):
        queue = deque([(u, 0)])  # (city, distance)
        while queue:
            city, d = queue.popleft()
            if city not in visited:
                visited.add(city)
                dist[city] = min(dist[city], d)
                for neighbor in graph[city]:
                    queue.append((neighbor, d+1))

    dfs(0)  # Start DFS from the capital (0th city)

    # Find the minimum number of roads to be reversed
    min_edges = float('inf')
    capitals = []
    for i, d in sorted(dist.items(), key=lambda x: x[1]):
        if d < min_edges:
            min_edges = d
            capitals = [i]
        elif d == min_edges:
            capitals.append(i)

    print(min_edges)
    print(*capitals, sep='\n')

# Example usage
n = int(input())
roads = [(int(x), int(y)) for x, y in [input().split() for _ in range(n-1)]]

invert Roads(n, roads)
