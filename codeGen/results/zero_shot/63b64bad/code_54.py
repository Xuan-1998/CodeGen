def simulate_program(a, n):
    y = 0
    x = 1
    while x <= n and x > 0:
        x += a[x]
        y += a[x]
        x -= a[x]
    return y

n = int(input())
a = list(map(int, input().split()))
for i in range(2, n+1):
    result = simulate_program(a[i-1:i], i)
    print(result)
