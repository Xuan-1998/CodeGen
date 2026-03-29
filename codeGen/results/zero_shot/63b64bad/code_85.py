import sys

n = int(sys.stdin.readline().strip())
sequence = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    max_x = 0
    for a in sequence[i:]:
        max_x += a
        if max_x > n:
            break
    if max_x <= n:
        print(max_x)
    else:
        print(-1)
