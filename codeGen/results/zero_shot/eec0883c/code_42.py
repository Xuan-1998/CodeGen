# Step 1: Read input
n = int(input())
gas_stations = list(map(int, input().split()))
roads = []
for i in range(n - 1):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))

# Step 2: Initialize maximum gasoline for each city
max_gasoline = [0] * (n + 1)
for i in range(1, n + 1):
    max_gasoline[i] = gas_stations[i - 1]

# Step 3: Use DFS to calculate maximum gasoline for each city
def dfs(u, parent):
    for v, c in roads:
        if v == u and v != parent:
            new_gasoline = min(max_gasoline[u], c)
            max_gasoline[v] = max(max_gasoline[v], new_gasoline + dfs(v, u))
    return max_gasoline[u]

# Step 4: Find the maximum gasoline at the end of the path
max_gasoline_at_end = max_gasoline[1]
print(max_gasoline_at_end)
