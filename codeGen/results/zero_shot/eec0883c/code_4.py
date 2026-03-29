import sys

def max_gasoline(n, w, roads):
    # Create a graph with negative weights representing the road lengths
    graph = {i: [] for i in range(1, n+1)}
    for u, v, c in roads:
        graph[u].append((v, -c))
        graph[v].append((u, -c))

    # Perform Dijkstra's algorithm to find the shortest path between two cities
    start = 1
    end = n
    dist = {i: float('inf') for i in range(1, n+1)}
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        d, u = heapq.heappop(queue)
        if d > dist[u]:
            continue
        for v, c in graph[u]:
            new_d = d + c
            if new_d < dist[v]:
                dist[v] = new_d
                heapq.heappush(queue, (new_d, v))

    # Find the maximum amount of gasoline that can be bought along the path
    max_gas = 0
    curr_gas = w[start]
    for i in range(start+1, end):
        if curr_gas <= dist[i]:
            break
        curr_gas -= dist[i]
        max_gas += w[i]

    return max_gas

# Read input from stdin
n = int(sys.stdin.readline())
w = [int(x) for x in sys.stdin.readline().split()]
roads = []
for i in range(n-1):
    u, v, c = map(int, sys.stdin.readline().split())
    roads.append((u, v, c))

# Calculate the maximum amount of gasoline
max_gas = max_gasoline(n, w, roads)

# Print the result to stdout
print(max_gas)
