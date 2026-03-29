import sys

def has_path(u, v):
    while u < v:
        if (u & v) != v:
            return False
        u = u | v
    return True

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print("YES" if has_path(u, v) else "NO")
