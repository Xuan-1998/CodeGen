def simulate_program(n, sequence):
    x = 1
    y = 0
    while x > 0 and x <= n:
        x += sequence[x-1]
        y += sequence[x-1]
        x -= sequence[x-1]
    return y if x > 0 else -1

n = int(input())
sequence = list(map(int, input().split()))
for i in range(1, n):
    print(simulate_program(n, [i] + sequence))
