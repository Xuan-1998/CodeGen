def simulate_program(a):
    x = 1
    y = 0
    while x <= len(a) and x > 0:
        x += a[x-1]
        y += a[x-1]
        if x > len(a):
            x -= a[x-1]
            y += a[x-1]
    return y

n = int(input())
a = list(map(int, input().split()))
for i in range(1, n+1):
    print(simulate_program(range(2, i+1)))
