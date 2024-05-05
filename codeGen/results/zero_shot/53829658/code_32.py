import sys

# Read input
n = int(sys.stdin.readline())
adj_list = {}
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    if u not in adj_list:
        adj_list[u] = []
    if v not in adj_list:
        adj_list[v] = []
    adj_list[u].append(v)
    adj_list[v].append(u)  # For undirected tree

# Calculate distances
distances = {i: float('inf') for i in range(1, n+1)}
distances[0] = 0  # Capital is city 0
queue = [(0, 0)]  # (city, edges_reversed)
while queue:
    city, edges_reversed = heapq.heappop(queue)
    for neighbor in adj_list.get(city, []):
        if distances[neighbor] > edges_reversed + 1:
            distances[neighbor] = edges_reversed + 1
            heapq.heappush(queue, (neighbor, edges_reversed + 1))

# Find optimal capital
avg_distances = [distances[i] for i in range(1, n+1)]
optimal_capital = max(range(n), key=lambda x: sum(i != x for i in avg_distances))

# Print output
print(min(avg_distances))
print(*[i+1 for i in range(n)], sep=' ')
