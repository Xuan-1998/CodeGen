def get_min_prime_divisor(n):
    # This function returns the minimum prime divisor of a number n
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            return i
    return n

def is_good_prime(n):
    # This function checks if a prime number n is good or bad
    return True  # replace with your implementation

def max_beauty():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    memo = {}

    def calculateBeauty(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        max_val = 0
        for k in range(i, j + 1):
            prime_divisor = get_min_prime_divisor(array[k])
            beauty_value = 1 if is_good_prime(prime_divisor) and prime_divisor not in bad_primes else -1
            val = calculateBeauty(i, k - 1) + beauty_value
            max_val = max(max_val, val)

        memo[(i, j)] = max_val
        return max_val

    return calculateBeauty(0, n - 1)

print(max_beauty())
