from functools import lru_cache
def max_beauty(A, bad_primes):
    @lru_cache(None)
    def Beauty(i, j):
        if i == j:
            return 0
        beauty = 0
        for k in range(i, j+1):
            is_good = all(p not in bad_primes for p in prime_factors(A[k]))
            beauty += (is_good) - (not is_good)
        return beauty

    @lru_cache(None)
    def max_beauty_subarray(i, j):
        if i == j:
            return 0
        if A[i] in bad_primes:
            return max_beauty_subarray(i+1, j)
        return Beauty(i, j)

    n = len(A)
    m = len(bad_primes)
    print(max_beauty_subarray(0, n-1))

