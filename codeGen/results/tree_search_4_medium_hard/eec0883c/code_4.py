import sys
from collections import defaultdict

# Read the number of cities
n = int(sys.stdin.readline().strip())

# Read the maximum amount of gasoline that Nut can buy in each city
w = list(map(int, sys.stdin.readline().split()))

# Read the road system (n-1 lines)
graph = defaultdict(list)
for _ in range(n-1):
    u, v, c = map(int, sys.stdin.readline().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

# Initialize the memo dictionary
memo = {}

def dfs(node, gas):
    if node not in memo:
        if len(graph[node]) == 0: # leaf node
            memo[node] = min(gas, w[node])
        else:
            memo[node] = max(gas - c for v, c in graph[node] + ((node,), 0) for _ in range(len(graph[node])) | {None})
    return memo[node]

# Start DFS from city 0
max_gas = 0
for child in graph[1]:
    max_gas = max(max_gas, dfs(1, w[0] - child[1]))

print(max_gas)
