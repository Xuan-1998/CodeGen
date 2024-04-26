import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, x, k = map(int, sys.stdin.readline().split())
    d = (k - 1) // k * k
    if d == x or d + k == x:
        print("YES")
    else:
        print("NO")
