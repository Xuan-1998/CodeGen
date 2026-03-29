def simulate_program(a):
    x = y = 1
    while True:
        x += a[x]
        y += a[x]
        x -= a[x]
        if x <= 0 or x > len(a) - 2:
            return y

n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
    print(simulate_program(list(range(2, n+1))[i:]))
