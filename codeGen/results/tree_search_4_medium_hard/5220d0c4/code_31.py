import sys

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
    return len(set(prime_factors)) == 1

n, m = map(int, input().split())
A = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

Beauty = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(i, n+1):
        if j - i + 1 == 1:
            Beauty[i][j] = is_good(prime_factors(A[i-1])) 
        else:
            Beauty[i][j] = max(Beauty[i-1][j], Beauty[i][j-1]) + (is_good(prime_factors(A[j-1])) - is_good(prime_factors(A[i-1])))
    for j in range(m+1):
        if bad_primes[j-1] < A[0]:
            Beauty[0][j] = 0
        else:
            Beauty[0][j] = -1

print(Beauty[-1][-1])
