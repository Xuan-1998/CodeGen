import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_min_prime_divisor(n):
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            return i
    return n

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        min_prime_divisor = find_min_prime_divisor(arr[i - 1])
        if min_prime_divisor not in bad_primes:
            max_beauty = dp[i - 1][bad_primes.index(min_prime_divisor)] if min_prime_divisor in bad_primes else dp[i - 1][-1]
            for j in range(m):
                if arr[i - 1] % bad_primes[j] == 0 and not is_prime(arr[i - 1]):
                    max_beauty = max(max_beauty, dp[i - 1][j])
        else:
            max_beauty = dp[i - 1][-1]

        for j in range(m):
            if arr[i - 1] % bad_primes[j] == 0 and not is_prime(arr[i - 1]):
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

        if min_prime_divisor not in bad_primes:
            dp[i][-1] = max(dp[i][-1], max_beauty)
        else:
            dp[i][-1] = dp[i - 1][-1]

    return dp[n][-1]

print(solve())
