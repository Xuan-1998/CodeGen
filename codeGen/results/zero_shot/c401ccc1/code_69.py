import sys

def is_path_exists(u, v):
    return u & v == v

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    if is_path_exists(u, v):
        print("YES")
    else:
        print("NO")
