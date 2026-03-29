import sys

def infinite_zoo_query(u, v):
    if u & v == v:
        return "YES"
    else:
        return "NO"

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print(infinite_zoo_query(u, v))
