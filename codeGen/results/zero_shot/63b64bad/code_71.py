code
n = int(input())
sequence = list(map(int, input().split()))
y_values = []

for sequence in [(1,) + tuple(map(int, input().split())) for _ in range(n - 1)]:
    x, y = 1, 0
    while x > 0 and x <= n:
        a_x = sequence[0]
        sequence = sequence[1:]
        x += a_x
        y += a_x
        if x > len(sequence):
            break
        x -= sequence[0]
        y += sequence[0]
    y_values.append(y)

print('\n'.join(map(str, y_values)))
