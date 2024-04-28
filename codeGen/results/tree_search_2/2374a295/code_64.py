def count_good_sequences():
    n, k = map(int, input().split())
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        s[i][1] = 1

    for j in range(2, n + 1):
        for i in range(j - 1, 0, -1):
            if i % j == 0:
                for j' in range(1, j // i + 1):
                    s[i][j] += s[i // j][j']

    print(sum(s[n][i] for i in range(1, k + 1)) % (10**9 + 7))

count_good_sequences()
