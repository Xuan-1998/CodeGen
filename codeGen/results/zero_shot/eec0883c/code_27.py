# Step 1: Read the input
n = int(input())
gasoline_amounts = list(map(int, input().split()))
roads = []
for _ in range(n - 1):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))

# Step 2: Create a graph and calculate the maximum flow for each city
from collections import defaultdict

graph = defaultdict(dict)
max_flow = [0] * n
for u, v, c in roads:
    graph[u][v] = c
    graph[v][u] = 0  # Assuming bidirectional roads
    max_flow[u] += c
    max_flow[v] += c

# Step 3: Use a BFS to find the maximum flow for each city
from collections import deque

def bfs(city, target):
    queue = deque([(city, max_flow[city])])
    visited = [False] * n
    while queue:
        current_city, current_gasoline = queue.popleft()
        if not visited[current_city]:
            visited[current_city] = True
            for neighbor in graph[current_city]:
                if neighbor == target and gasolina_amounts[neighbor] - max_flow[neighbor] + current_gasoline >= 0:
                    return current_gasoline
                if not visited[neighbor] and gasolina_amounts[neighbor] - max_flow[neighbor] + current_gasoline >= 0:
                    queue.append((neighbor, min(current_gasoline, gasolina_amounts[neighbor] - max_flow[neighbor])))
    return 0

# Step 4: Calculate the maximum flow for each city and update the answer
answer = 0
for i in range(1, n):
    answer = max(answer, bfs(0, i))

print(answer)
