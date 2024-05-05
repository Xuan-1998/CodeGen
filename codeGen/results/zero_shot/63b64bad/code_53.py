def simulate_program(a):
    x, y = 1, 0
    while x > 0 and x <= len(a):
        x += a[x]
        y += a[x]
        x -= a[x]
    return y

n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    print(simulate_program(a[i-1:i+1]))
