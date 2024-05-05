import sys

def can_reach(u, v):
    while u > 0:
        if u & v == 0:
            return False
        u = u & (u - 1)
    return True

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print("YES" if can_reach(u, v) else "NO")
