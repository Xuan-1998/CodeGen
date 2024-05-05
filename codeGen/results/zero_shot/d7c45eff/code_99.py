import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

if k <= n:
    print(s[-k:])
else:
    if k % 2 == 0:
        print(s * (k // 2))
    else:
        print((s + s)[:k])
