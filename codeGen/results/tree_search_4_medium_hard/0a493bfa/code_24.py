from functools import lru_cache

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

@lru_cache(None)
def f(s, bad_primes):
    p = min((p for p in range(2, s + 1) if all(p % x for x in range(x, s + 1)) and p not in bad_primes), default=s)
    return f(s // p, bad_primes) - s if p else 0

def max_beauty(n, m, a, bad_primes):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(m + 1):
            if i == 1:
                dp[i][j] = f(a[0], bad_primes)
            else:
                left_max = max(dp[i - 1][j])
                right_max = max(dp[n - i][j])
                dp[i][j] = max(left_max, right_max) + a[i - 1]
    
    return max(dp[n])

n, m = map(int, input().split())
a = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(n, m, a, bad_primes))
