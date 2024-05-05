import sys

def find_path(u, v):
    while u != v:
        if not (u & v):  # If there is no edge between u and v
            return "NO"
        u = v
    return "YES"

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print(find_path(u, v))
