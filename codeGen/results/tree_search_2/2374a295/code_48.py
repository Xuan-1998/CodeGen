def count_good_sequences(n, k):
    memo = [0] * (n + 1)
    memo[1] = 1

    for i in range(2, n + 1):
        if all(i % j == 0 for j in range(2, i)):
            memo[i] = sum(memo[j] for j in range(1, i))
        else:
            memo[i] = 0

    return memo[n] % 100000007
