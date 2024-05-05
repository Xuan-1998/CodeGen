import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def max_beauty(n, m, a, bad_primes):
    memo = {}

    def dfs(i, bad_primes):
        if (i, tuple(sorted(bad_primes))) in memo:
            return memo[(i, tuple(sorted(bad_primes)))]
        
        beauty = 0
        for j in range(i+1, n+1):
            gcd_sum = sum(math.gcd(a[i], a[j]) for k in range(j+1, n+1) if math.gcd(a[i], a[k]) == math.gcd(a[i], a[j]))
            
            bad_prime = False
            for p in bad_primes:
                if p in [math.gcd(a[i], a[j]), math.gcd(a[i], a[k])] or gcd_sum % p == 0:
                    bad_prime = True
                    break
            
            if not bad_prime and gcd_sum > beauty:
                beauty = gcd_sum
        
        memo[(i, tuple(sorted(bad_primes)))] = max(beauty, dfs(i-1, bad_primes + (a[i],)))
        return memo[(i, tuple(sorted(bad_primes)))]

    return dfs(n-1, set())

n, m = map(int, input().split())
a = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(n, m, a, bad_primes))
