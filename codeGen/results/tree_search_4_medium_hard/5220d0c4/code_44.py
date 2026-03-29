def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            while n % i == 0:
                n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def is_good(prime_factors):
    for prime in prime_factors:
        if prime in bad_primes:
            return False
    return True

bad_primes = set()
max_beauty = {}

def max_beauty_recursive(i, j):
    if (i, j) in max_beauty:
        return max_beauty[(i, j)]
    if i > j:
        return 0
    if is_good(prime_factors(A[i])):
        return max_beauty_recursive(i+1, j) + 1
    else:
        return max(max_beauty_recursive(i-1, j), max_beauty_recursive(i, j-1)) - 1

n, m = map(int, input().split())
A = list(map(int, input().split()))
bad_primes = set(map(int, input().split()))

print(max_beauty_recursive(0, n-1))
