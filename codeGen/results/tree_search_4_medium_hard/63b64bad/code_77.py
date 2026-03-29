def simulate_sequence(n, sequence):
    max_y = max(sequence)
    dp = [[-1 for _ in range(max_y + 1)] for _ in range(n + 1)]

    for i in range(2, n + 1):
        x, y = i - 1, 0
        while x <= 0 or x > n:
            if x > n:
                return y
            x += sequence[x]
            y += sequence[x] * (x != 0)
            x -= sequence[x]

    for i in range(n - 2, -1, -1):
        x, y = i, dp[i + 1][y]
        while x <= 0 or x > n:
            if x > n:
                return y
            x += sequence[x]
            y += sequence[x] * (x != 0)
            x -= sequence[x]

    return -1

n = int(input())
sequence = list(map(int, input().split()))
for i in range(n - 1):
    print(simulate_sequence(i + 2, sequence[i + 2:]))
