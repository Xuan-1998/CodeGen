import sys
from collections import defaultdict

# Read input
n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# Step 1: Find all strongly connected components (SCCs) using Tarjan's algorithm
sccs = []
lowlinks = {}
index = 0
stack = set()
for node in range(1, n + 1):
    if node not in lowlinks:
        scc = []
        index += 1
        lowlink = index
        stack.add(node)
        lowlinks[node] = index
        while node in stack:
            for neighbor in graph[node]:
                if neighbor not in lowlinks:
                    lowlinks[neighbor] = index + 1
                    stack.add(neighbor)
                    node = neighbor
                elif neighbor in stack:
                    lowlink = min(lowlink, lowlinks[neighbor])
            stack.remove(node)
        sccs.append(scc)

# Step 2: Compute the maximum beauty for each SCC
beauties = []
for scc in sccs:
    max_beauty = len(scc) * (n - len(scc))
    beauties.append(max_beauty)

# Step 3: Combine the maximum beauties of all SCCs and find the maximum possible value
max_beauty = sum(beauties)
print(max_beauty)
