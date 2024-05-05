import sys

q = int(sys.stdin.readline())
dp = {0: True}

for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    while v > 0:
        if (v & 1) and dp.get(v ^ 1):
            print("YES")
            break
        v >>= 1
    else:
        print("NO")
