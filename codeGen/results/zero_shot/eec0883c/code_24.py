# Step 1: Read the input
n = int(input())
w = list(map(int, input().split()))
roads = []
for _ in range(n-1):
    u, v, c = map(int, input().split())
    roads.append((u-1, v-1, c))

# Step 2: Perform DFS and calculate the maximum gasoline at each node
gasoline_at_node = [0]*n
for u, v, c in roads:
    if gasoline_at_node[u] + w[u] > gasoline_at_node[v]:
        gasoline_at_node[v] = gasoline_at_node[u] + w[u]
    else:
        gasoline_at_node[v] = gasoline_at_node[v] - c

# Step 3: Find the maximum gasoline at the end of the path
max_gasoline = max(gasoline_at_node)

print(max_gasoline)
