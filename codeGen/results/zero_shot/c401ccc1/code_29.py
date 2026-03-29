import sys

def zookeeper_query(u, v):
    while u != v:
        if (u & v) != v:
            return "NO"
        u = v
        v = v & u
    return "YES"

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print(zookeeper_query(u, v))
