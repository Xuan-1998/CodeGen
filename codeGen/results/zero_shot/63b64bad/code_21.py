n = int(input())
sequence = list(map(int, input().split()))

for i in range(1, n+1):
    x, y = 1, 0
    while True:
        if x <= 0 or x > n:
            break
        x += sequence[x]
        y += sequence[x]
        x -= sequence[x]
    print(y)
