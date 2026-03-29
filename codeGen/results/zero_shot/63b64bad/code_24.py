n = int(input())
x, y = 1, 0

sequence = [int(x) for x in input().split()]

for a in sequence[1:]:
    for _ in range(a):
        x, y = y + a, x
    if x <= 0 or x > n:
        print(-1)
    else:
        print(y)
