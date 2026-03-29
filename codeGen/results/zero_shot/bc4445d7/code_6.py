import math

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    prime_factors = [p for p in range(2, n) if primes[p]]
    return prime_factors

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        u_v_edges = []
        for _ in range(n-1):
            u, v = map(int, input().split())
            u_v_edges.append((u, v))
        
        k = int(input())
        prime_factors = sieve_of_eratosthenes(math.isqrt(k) + 1)
        if not any(p <= k for p in prime_factors):
            print(0)
        else:
            max_distribution_index = 0
            for i in range(len(prime_factors)):
                for j in range(i+1, len(prime_factors)):
                    product = 1
                    for edge in u_v_edges:
                        if math.gcd(edge[0], edge[1]) == 1:
                            product *= prime_factors[i]
                        else:
                            product *= prime_factors[j]
                    distribution_index = sum(math.log10(p) for p in (prime_factors[i], prime_factors[j])) - math.log10(product)
                    max_distribution_index = max(max_distribution_index, distribution_index)
            print(int(max_distribution_index % (10**9 + 7)))

if __name__ == "__main__":
    solve()
