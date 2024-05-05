import sys

def check_path(u, v):
    for w in range(2**30):
        if u & w == v:
            return True
    return False

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print("YES" if check_path(u, v) else "NO")
