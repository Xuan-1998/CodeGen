def max_beauty(n, primes, bad_primes):
    dp = [[0] * (len(bad_primes) + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if is_good_prime(i, primes, bad_primes):
            dp[i][0] = min(dp[max(0, i - 1)][0], i)
        else:
            dp[i][0] = 0

        for j in range(1, len(bad_primes) + 1):
            if is_bad_prime(bad_primes[j - 1]):
                dp[i][j] = max(dp[max(0, i - 1)][j], dp[i][j - 1])
            else:
                dp[i][j] = dp[i][j - 1]

    return dp[n][-1]


def is_good_prime(num, primes, bad_primes):
    for prime in primes:
        if num % prime == 0 and prime not in bad_primes:
            return True
    return False


def is_bad_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

# Read input from standard input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(n, arr, bad_primes))
