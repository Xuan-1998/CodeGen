def simulate_program(n, sequence):
    x = 1
    y = 0
    while True:
        if x <= 0 or x > n:
            return -1
        x += sequence[x]
        y += sequence[x]
        x -= sequence[x]

n = int(input())
sequence = list(map(int, input().split()))
for i in range(2, n + 1):
    result = simulate_program(i, [0] + sequence[:i])
    if result == -1:
        print(-1)
    else:
        print(result)
