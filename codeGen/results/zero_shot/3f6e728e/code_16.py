def count_x_sequences(n, m):
    upper_radii = set()
    lower_radii = set()

    for _ in range(n):
        radius = int(input())
        upper_radii.add(radius)

    for _ in range(m):
        radius = int(input())
        lower_radii.add(radius)

    x_sequences = 1
    for i in range(1, C + 1):
        x_sequences *= (upper_radii & {i}) | (lower_radii & {i})

    return x_sequences % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, m, c = map(int, input().split())
    print(count_x_sequences(n, m))
