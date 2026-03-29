def simulate_program(a):
    x, y = 1, 0
    while x <= n and x > 0:
        x += a[x]
        y += a[x]
        x -= a[x]
    return y if x > 0 else -1

n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
    print(simulate_program(a[i+2]))
