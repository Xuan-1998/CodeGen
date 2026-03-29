def expected_carries(N):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    memo = {}

    def carry(i, j):
        if (i, j) not in memo:
            if i == 0 or j == 0:
                memo[(i, j)] = 0
            else:
                total_sum = int(str(10 ** (i - 1)) + str(int((10 ** N) * A % 10) + B % 10))
                memo[(i, j)] = 1 if total_sum >= 10 else 0
        return memo[(i, j)]

    cum_carries = 0

    for i in range(1, N + 1):
        for j in range(1, min(i, N) + 1):
            cum_carries += carry(i, j)

    return cum_carries / (N ** 2)
