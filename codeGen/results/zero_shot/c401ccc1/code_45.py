import sys
q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    if (u & v) == v:
        print("YES")
    else:
        print("NO")
