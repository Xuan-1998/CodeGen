n = int(input())
sequence = list(map(int, input().split()))

for a in sequence[1:]:
    x, y = 1, 0
    while True:
        if x <= 0 or x > n:
            break
        x += a
        y += a
        x -= a
    final_y = y
    print(final_y)
