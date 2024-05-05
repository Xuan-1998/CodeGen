import sys

def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]"
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if prime[p]]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def f(s):
    good_primes = set()
    for p in range(2, s + 1):
        if all(p != b and is_prime(b) for b in range(2, int(p ** 0.5) + 1)):
            good_primes.add(p)
    return sum(good_primes)

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Find all prime numbers less than or equal to max(b) that are not in the set b
    good_primes = set()
    for p in range(2, max(b) + 1):
        if all(p != b and is_prime(b) for b in range(2, int(p ** 0.5) + 1)):
            good_primes.add(p)
    
    # Calculate the beauty of the array
    beauty = f(sum(a))
    return str(beauty)

def is_prime(n):
    if n < 2:
        return False
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    return True

if __name__ == "__main__":
    print(solve())
