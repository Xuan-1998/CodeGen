import sys
n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
for i in range(2, n+1):
    x, y = 1, 0
    while True:
        if x <= 0 or x > i:
            print(-1)
            break
        x += sequence[x]
        y += sequence[x]
        x -= sequence[x]
    else:
        print(y)
