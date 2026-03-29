n = int(input())
sequence = list(map(int, input().split()))

y_values = []
for a in sequence[1:]:
    x, y = 1, 0
    while x <= n and x > 0:
        x += a
        y += a
        x -= a
    if x > 0:
        y_values.append(y)
    else:
        y_values.append(-1)

print('\n'.join(map(str, y_values)))
