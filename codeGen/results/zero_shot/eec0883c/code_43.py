# Step 1: Understand the problem
# A simple path between two cities means we need to find a path with minimum total length (or maximum gas left)

# Step 2: Initialize variables
n, *gas_stations = map(int, input().split())  # Read number of cities and max gas for each city

# Step 3: Build the tree structure
roads = []
for _ in range(n - 1):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))  # Store road edges in a list

# Step 4: Perform DFS to find maximum gas for each city
max_gas_per_city = [0] * (n + 1)
visited = [False] * (n + 1)

def dfs(city):
    if visited[city]:
        return max_gas_per_city[city]
    visited[city] = True
    max_gas_per_city[city] = gas_stations[city - 1]
    for neighbor, cost in roads:
        if neighbor == city:
            next_max_gas = min(dfs(neighbor), gas_stations[city - 1] - cost)
            max_gas_per_city[city] = max(max_gas_per_city[city], next_max_gas + cost)
    return max_gas_per_city[city]

# Step 5: Find the maximum gas along a path from city 1 to city n
print(dfs(1))
