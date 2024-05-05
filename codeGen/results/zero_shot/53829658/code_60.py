import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for i in range(1, n):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)

root = 0
max_children = 0

# Find the root city (capital) that is most centrally located
for i in range(1, n+1):
    children = len(graph[i])
    if children > max_children:
        max_children = children
        root = i

sys.stdout.write(str(max_children) + '\n')

# Traverse the tree starting from the root city and keep track of reversals
reversals = [0] * (n+1)

for i in range(1, n+1):
    if graph[i]:
        parent = graph[i][0]
        while parent != 0:
            reversals[parent] += 1
            parent = graph[parent][0]

sys.stdout.write(' '.join(map(str, reversals)) + '\n')
