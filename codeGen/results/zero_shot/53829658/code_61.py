# Read the number of cities
n = int(input())

# Create an adjacency list representation of the directed tree
tree = {}
for i in range(n-1):
    u, v = map(int, input().split())
    if u not in tree:
        tree[u] = []
    if v not in tree:
        tree[v] = []
    tree[u].append(v)

# Perform a DFS to find the root of the tree (the capital city)
capital = None
visited = set()
def dfs(node):
    visited.add(node)
    for neighbor in tree[node]:
        if neighbor not in visited:
            dfs(neighbor)
    return node

for city in tree:
    if city not in visited:
        capital = city
        break

# Perform a DFS from each node to find the maximum distance from that node
distances = {}
def dfs_max_distance(node):
    visited = set()
    max_dist = 0
    def dfs_max_dist(node, dist):
        nonlocal max_dist
        visited.add(node)
        if dist > max_dist:
            max_dist = dist
        for neighbor in tree[node]:
            if neighbor not in visited:
                dfs_max_dist(neighbor, dist+1)
    dfs_max_dist(node, 0)
    return max_dist

max_distances = {city: dfs_max_distance(city) for city in tree}

# Choose the capital city that minimizes the maximum distance
min_max_distance = min(max_distances.values())
capital_cities = [city for city, dist in max_distances.items() if dist == min_max_distance]

# Print the minimum number of roads to be reversed and all possible ways to choose the capital
print(min_max_distance)
print(' '.join(map(str, capital_cities)))
