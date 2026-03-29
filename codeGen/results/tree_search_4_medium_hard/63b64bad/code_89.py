def simulate_program(a):
    x, y = 1, 0
    while 1 <= x <= len(a):
        a[x-2] -= 1  # Update x and y
        if a[x-2] == 0:
            break
        x += a[x-2]
        y += a[x-2]
    return y

n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    print(simulate_program(a))
