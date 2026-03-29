# Step 1: Read the input
n = int(input())
w = list(map(int, input().split()))
edges = []
for i in range(n-1):
    u, v, c = map(int, input().split())
    edges.append((u, v, c))

# Step 2: Create a tree data structure
tree = {}
parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

for i in range(n):
    make_set(i)

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(u, v):
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_u] = root_v
            if rank[root_u] == rank[root_v]:
                rank[root_v] += 1

for u, v, c in edges:
    union(u, v)

# Step 3: Calculate the maximum amount of gasoline
gasoline = [0] * n
max_gasoline = 0
for i in range(n):
    for j in range(i+1, n):
        if find(i) == find(j):
            gasoline[j] = min(gasoline[i], w[i] - c)
            max_gasoline = max(max_gasoline, gasoline[j])

# Step 4: Print the answer
print(max_gasoline)
