n = int(input())
sequence = list(map(int, input().split()))

for i in range(2, n+1):
    x, y = 1, 0
    while True:
        a_value = sequence[i-1]
        x += a_value
        y += a_value
        x -= a_value
        if x <= 0 or x > n:
            break
    print(y)
