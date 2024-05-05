def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            for j in range(2, int(n**0.5) + 1):
                if n % (i*j):
                    break
            else:
                n //= i
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return set(factors)

def is_good(primes):
    for prime in primes:
        if prime in bad_primes:
            return False
    return True

n, m = map(int, input().split())
A = list(map(int, input().split()))
bad_primes = set(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    dp[i][i] = 0 if A[i] in bad_primes else 1
for length in range(2, n+1):
    for i in range(n-length):
        j = i + length - 1
        dp[i][j] = max((is_good(prime_factors(A[k])) for k in range(i, j+1))) 

print(dp[0][n-1])
