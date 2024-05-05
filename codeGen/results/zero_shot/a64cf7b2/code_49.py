python
n, m, T = map(int, input().split())
edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

in_degree = [0] * (n + 1)
for u, v, t in edges:
    in_degree[v] += 1

queue = [(u, t) for u, t in enumerate(in_degree) if u == 1 or t == 0]
while queue:
    u, t = queue.pop(0)
    if u > n: break
    for v, wt in edges:
        if u == v and wt <= T - t:
            T -= wt
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append((v, t + wt))

k = sum(1 for _ in range(n) if _ == i)

print(k)
for i in range(n):
    if i == k - 1:
        print(i + 1)
        break
