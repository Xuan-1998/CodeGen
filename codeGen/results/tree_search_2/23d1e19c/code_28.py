def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    root_x = find_parent(parent, x)
    root_y = find_parent(parent, y)

    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    union_parent(parent, u, v)

k = int(input())
path = list(map(int, input().split()))
min_recompute, max_recompute = 0, 0

for i in range(k-1):
    v, t = path[i], path[i+1]
    if find_parent(parent, v) != find_parent(parent, t):
        min_recompute += 1
    max_recompute = max(max_recompute, min_recompute)

print(min_recompute, max_recompute)
