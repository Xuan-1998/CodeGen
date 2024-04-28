def count_good_sequences(n, k):
    mod = 1000000007
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        if i % k == 0:
            dp[i][0] = sum(1 for _ in range(2, min(i + 1, n) + 1) if primes[_])
        for j in range(1, k + 1):
            dp[i][j] = (dp[i - 1][j - 1] + int(primes[j])) % mod

    return dp[n][k]
