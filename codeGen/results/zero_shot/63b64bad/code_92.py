n = int(input())
sequence = list(map(int, input().split()))

for x in range(1, n+1):
    y = 0
    while True:
        if x <= 0 or x > n:
            print(-1)
            break
        x += sequence[x]
        y += sequence[x]
        x -= sequence[x]
    print(y)
