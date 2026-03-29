import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    values = list(map(int, sys.stdin.readline().split()))
    graph = {}
    components = 1
    for i in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        xor_val = values[u] ^ values[v]
        if xor_val != 0:
            components += 1
            graph[u] = v
            graph[v] = u
    if components > k:
        return "NO"
    else:
        return "YES"

print(solve())
