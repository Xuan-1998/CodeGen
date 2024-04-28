def count_good_sequences(n, k):
    s = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        s[i][1] = 1

    for j in range(2, k + 1):
        for i in range(1, n // j + 1):
            for j_divisor in range(j - 1, 0, -1):
                if i * j_divisor <= n:
                    s[i][j] += s[i * j_divisor][j_divisor]
            s[i][j] %= 1000000007

    return sum(s[i][k] for i in range(1, n + 1)) % 1000000007
