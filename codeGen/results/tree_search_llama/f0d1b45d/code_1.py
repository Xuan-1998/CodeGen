from collections import defaultdict

n = int(input())
parent_to_child = defaultdict(list)
child_to_parent = {}
visited = set()

def dfs(node):
    visited.add(node)
    for child in parent_to_child[node]:
        if child not in visited:
            dfs(child)

for _ in range(n):
    i, p = map(int, input().split())
    parent_to_child[p].append(i)
    child_to_parent[i] = p

trees = 0
for i in range(1, n + 1):
    if i not in visited:
        trees += 1
        dfs(i)

print(trees)
