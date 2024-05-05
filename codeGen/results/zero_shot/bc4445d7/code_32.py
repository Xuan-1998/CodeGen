import sys
input = lambda: map(int, input().split())

n, m = map(int, input().split())
i = 0
edges = []
children = [0] * n
labels = [0] * (n-1)
res = 0

for _ in range(n-1):
    u, v = map(int, input().split())
    edges.append((u,v))
    children[u] += 1
    children[v] += 1

for i in range(n-1):
    while i < n and edges[i][0] == edges[i-1][1]:
        f = 1
        for j in range(i+1, n):
            if edges[j][0] == edges[i][1] or edges[j][1] == edges[i][1]:
                f *= labels[i]
        res += f

print(res % (10**9 + 7))

