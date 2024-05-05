def simulate_program(a):
    x = 1
    y = 0
    while x > 0 and x <= len(a):
        x += a[x] - 1
        y += a[x]
    return y if x > 0 else -1

n = int(input())
a = list(map(int, input().split()))
for i in range(2, n+1):
    print(simulate_program(a[i-2:i]))
