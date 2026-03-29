import sys

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root != y_root:
        parent[y_root] = x_root

parent = {}
ans = []

while True:
    try:
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        for _ in range(n - 1):
            u, v = map(int, input().split())
            if u not in parent: parent[u] = u
            if v not in parent: parent[v] = v
            union(parent, u, v)
    except:
        break

for x in set(list(parent.keys())):
    if len(set([find(parent, y) for y in [u for u in range(1, n + 1) if parent[u] == x]])) > 1:
        ans.append("NO")
    else:
        xor = a[0]
        for i in set(list(parent.keys())):
            if find(parent, i) == x:
                xor ^= a[i - 1]
        for y in [u for u in range(1, n + 1) if parent[u] == x]:
            if a[y - 1] != xor:
                ans.append("NO")
                break
        else:
            ans.append("YES")

print("\n".join(ans))
