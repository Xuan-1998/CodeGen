import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

for i in range(2, n+1):
    x = 1
    y = 0
    while x > 0 and x <= n:
        x += sequence[i-1]
        y += sequence[i-1]
        x -= sequence[i-1]
    if x <= 0 or x > n:
        print(-1)  # program terminated, print -1
    else:
        print(y)  # program didn't terminate, print final value of y
