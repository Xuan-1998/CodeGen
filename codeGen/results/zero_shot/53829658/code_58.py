# Step 1: Read the input
n = int(input())
roads = []
for _ in range(n-1):
    si, ti = map(int, input().split())
    roads.append((si, ti))

# Step 2: Calculate the lowest reachable node for each node
lowest_reachable = [0] * (n+1)
parent = [-1] * (n+1)

for i in range(1, n):
    for si, ti in roads:
        if parent[ti] == -1 and lowest_reachable[si] < lowest_reachable[ti]:
            parent[ti] = si
            lowest_reachable[ti] = lowest_reachable[si]

# Step 3: Calculate the centroid of the tree
centroid = sum(lowest_reachable) // (n-1)

print(centroid)
