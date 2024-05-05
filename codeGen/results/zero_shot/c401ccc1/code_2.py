import sys

def infinite_zoo(u, v):
    while u > 0 and v > 0:
        if u & v == 0:
            return "NO"
        u >>= 1
        v &= (v - 1)
    return "YES"

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print(infinite_zoo(u, v))
