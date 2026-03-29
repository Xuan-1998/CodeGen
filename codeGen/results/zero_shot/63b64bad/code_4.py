code
n = int(input())
seq = list(map(int, input().split()))
for x in seq[1:]:
    x -= 1
    y = 0
    while True:
        if x <= 0 or x > n:
            print(-1)
            break
        x += a_x
        y += a_x
        x -= a_x
    print(y)
