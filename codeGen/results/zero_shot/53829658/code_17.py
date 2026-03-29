import sys

n = int(sys.stdin.readline())
out_degrees = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    out_degrees[u] += 1
    out_degrees[v] += 1

min_out_degree = min(out_degrees[1:])
capital = out_degrees.index(min(out_degrees[1:])) + 1

print(min_out_degree)
print(capital)
