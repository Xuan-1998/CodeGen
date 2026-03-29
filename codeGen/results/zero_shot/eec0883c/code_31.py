import sys

n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))

for _ in range(n - 1):
    u, v, c = map(int, sys.stdin.readline().split())
    w[v] = min(w[v], w[u] - c)

print(min(w))
