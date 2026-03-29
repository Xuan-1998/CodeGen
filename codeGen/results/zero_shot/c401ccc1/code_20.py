import sys

def solve(u, v):
    while u:
        if u & v != v:
            return "NO"
        u &= v
    return "YES"

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print(solve(u, v))
