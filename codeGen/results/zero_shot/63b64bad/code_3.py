import sys
n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
y_values = []
x = 1
y = 0
while x <= n:
    y += sequence[x]
    x += sequence[x]
    if x == y + 1:
        break
    y -= sequence[x - 1]
    x -= sequence[x - 1]
if x > n:
    print(-1)
else:
    for i in range(1, n):
        y_values.append(y)
        x = 1
        y = 0
        while x <= n:
            y += sequence[x]
            x += sequence[x]
            if x == y + 1:
                break
            y -= sequence[x - 1]
            x -= sequence[x - 1]
    for i in range(len(y_values)):
        print(y_values[i])
