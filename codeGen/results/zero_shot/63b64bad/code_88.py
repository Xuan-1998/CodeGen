def simulate_program(a):
    x = 1
    y = 0
    previous_values = []
    while True:
        if x <= 0 or x > len(a):
            break
        new_x = (x + a[x] - 1) % len(a)
        new_y = y + a[x]
        if [new_x, new_y] in previous_values:
            break
        x = new_x
        y = new_y
        previous_values.append([x, y])
    return y

n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
    print(simulate_program(a))
