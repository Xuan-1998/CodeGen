import sys

# Read input
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

# Function to find smallest prime factor of a number
def smallest_prime_factor(n):
    if n < 2:
        return n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i

# Calculate beauty score of each element
beauty_score = 0
for num in arr:
    min_prime_factor = smallest_prime_factor(num)
    if min_prime_factor in bad_primes:
        beauty_score -= num
    else:
        beauty_score += max(prime_factors(num))

print(beauty_score)

def prime_factors(n):
    factors = set()
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)
    return factors

def max_prime_factor(n):
    factors = prime_factors(n)
    return max(factors)

