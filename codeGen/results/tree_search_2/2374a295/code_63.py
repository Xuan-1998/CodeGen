def find_good_sequences():
    n, k = map(int, input().split())
    mod = 1000000007

    s = [[0] * (k + 1) for _ in range(n + 1)]

    # Base case: s[i, 1] = 1 for all i
    for i in range(1, n + 1):
        s[i][1] = 1

    for j in range(2, k + 1):
        for i in range(j - 1, n // j, -1):
            # Calculate the sum of good sequences ending with any multiple of i that is also a multiple of j
            s[i][j] = (sum(s[m][j - 1] for m in range(i, n // j + 1)) % mod)

    return s[n][k]

print(find_good_sequences())
