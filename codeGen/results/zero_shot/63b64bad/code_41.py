def simulate_program(a):
    x = 1
    y = 0
    while x <= n and x > 0:
        x += a[x]
        y += a[x]
        x -= a[x]
    return -1 if (x <= 0 or x > n) else y

n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    print(simulate_program(a)) 
