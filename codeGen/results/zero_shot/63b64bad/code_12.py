def simulate_program(a):
    x = y = 1
    while True:
        x += a[x]
        y += a[x]
        x -= a[x]
        if x <= 0 or x > len(a):
            return y

n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
    result = simulate_program(a[i])
    print(result)
