def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def f(s):
    p = min([i for i in range(2, s+1) if s % i == 0])
    good_prime = all(i not in bad_primes for i in [p] + list(range(2, int(s**0.5)+1)))
    return f(s//p) - s if not good_prime else f(s//p) + s

def solve(n, a, bad_primes):
    memo = {}
    
    def dp(i, j):
        key = (i, j)
        if key in memo:
            return memo[key]
        
        if i == 0 or j >= len(bad_primes):
            return 0
        
        if j < len(bad_primes) and bad_primes[j] > a[i]:
            dp(i-1, j)
        
        max_beauty = f(a[0:i+1])
        for k in range(1, i+1):
            max_beauty = max(max_beauty, dp(k-1, j) + f(gcd(a[k], *bad_primes[:j])))
        
        memo[key] = max_beauty
        return max_beauty
    
    return dp(n-1, 0)

n, m = map(int, input().split())
a = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(solve(n, a, bad_primes))
