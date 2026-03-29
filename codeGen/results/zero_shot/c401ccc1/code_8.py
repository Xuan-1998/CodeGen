import sys

def query(u, v):
    while u & v:
        if u == v:
            return "YES"
        u = u & (v - 1)
    return "NO"

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print(query(u, v))
