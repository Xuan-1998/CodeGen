def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def is_good(prime_factors):
    # This function should check whether the prime factors are good or bad primes
    pass

def max_beauty(A, bad_primes):
    n = len(A)
    maxBeauty = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if all(f not in bad_primes for f in prime_factors(A[i-1])):
                maxBeauty[i][j] = max(maxBeauty[i-1][j], maxBeauty[i][j-1]) + (is_good(prime_factors(A[i-1])) ? 1 : -1)
            else:
                maxBeauty[i][j] = max(maxBeauty[i-1][j], maxBeauty[i][j-1])
    
    return maxBeauty[n][n]

if __name__ == "__main__":
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))
    print(max_beauty(A, bad_primes))
