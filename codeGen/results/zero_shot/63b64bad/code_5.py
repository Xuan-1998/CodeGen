def simulate_program(a):
    x = 1
    y = 0

    while x > 0 and x <= len(a):
        x += a[x]
        y += a[x]
        x -= a[x]

    if x > 0:
        return -1
    else:
        return y


n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    print(simulate_program(a))
