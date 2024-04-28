n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
p = list(map(int, input().split()))

