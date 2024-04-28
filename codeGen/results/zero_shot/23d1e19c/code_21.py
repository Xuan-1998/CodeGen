n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))

min_recompute = float('inf')
max_recompute = 0

i = 1
while i < k:
    j = path[i]
    for next in graph[j]:
        if next == path[i+1]:
            min_recompute = min(min_recompute, 1)
            max_recompute = max(max_recompute, 2)
            break
    i += 1

print(min_recompute, max_recompute)
