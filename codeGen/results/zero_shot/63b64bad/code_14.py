def simulate_program(a):
    x = 1
    y = 0
    while x > 0:
        x += a[x]
        y += a[x]
        x -= a[x]
    return y

n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
    print(simulate_program(a))
