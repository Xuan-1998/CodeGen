n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)

k = int(input())
path = [int(x) - 1 for x in input().split()]
