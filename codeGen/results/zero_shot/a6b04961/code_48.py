import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# Initialize variables to keep track of the maximum beauty and the current tail length
max_beauty = 0
tail_length = 0

# Use DFS to find the maximum beauty
def dfs(node, parent, visited):
    global max_beauty, tail_length
    visited.add(node)
    
    # Find the longest path from this node to a leaf node
    for neighbor in graph[node]:
        if neighbor == parent:
            continue
        if neighbor not in visited:
            temp_tail_length = 1 + dfs(neighbor, node, set())
            if temp_tail_length > tail_length:
                tail_length = temp_tail_length
                max_beauty = max(max_beauty, tail_length * (n - len(visited)))
    
    return tail_length

# Start DFS from each unvisited node
for node in range(n):
    if node not in visited:
        dfs(node, -1, set())

print(max_beauty)
