# Step 1: Read the input
import sys

n = int(sys.stdin.readline().strip())
gas_stations = list(map(int, sys.stdin.readline().strip().split()))
roads = []
for _ in range(n-1):
    u, v, c = map(int, sys.stdin.readline().strip().split())
    roads.append((u-1, v-1, c))

# Step 2: Find the shortest path from root to each node
root = 0
parent = [-1]*n
max_gas = [0]*n

def dfs(node):
    if parent[node] == -1:
        return w[node]
    else:
        return min(dfs(parent[node]), c) + gas_stations[node]

for i in range(n):
    max_gas[i] = dfs(i)

# Step 3: Find the maximum amount of gasoline
max_amount = max(max_gas)
