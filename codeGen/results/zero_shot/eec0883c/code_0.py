# Step 1: Read the input
n = int(input())
w = list(map(int, input().split()))
edges = []
for _ in range(n-1):
    u, v, c = map(int, input().split())
    edges.append((u, v, c))

# Step 2: Create a disjoint set and find the root of each city
parent = {}
for i in range(1, n+1):
    parent[i] = i

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# Step 3: Merge cities with a road between them
for u, v, c in edges:
    ru = find(u)
    rv = find(v)
    if ru != rv:
        parent[rv] = ru

# Step 4: Calculate the maximum amount of gasoline that Nut can have at the end of the path
max_gasoline = 0
for city in range(1, n+1):
    city_gasoline = w[city-1]
    for edge in edges:
        if edge[0] == city or edge[1] == city:
            u, v, c = edge
            if find(u) == find(v):
                city_gasoline -= 1

    max_gasoline = max(max_gasoline, city_gasoline)

print(max_gasoline)
