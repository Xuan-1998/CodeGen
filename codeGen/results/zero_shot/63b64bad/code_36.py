n = int(input())
sequence = list(map(int, input().split()))
for i in range(n-1):
    x, y = 1, 0
    while True:
        if x <= 0 or x > n:
            break
        a = sequence[x]
        x += a
        y += a
        x -= a
    print(y)
