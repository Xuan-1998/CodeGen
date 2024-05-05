import math

def min_prime_divisor(n):
    if n <= 1:
        return None
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n

def max_beauty(n, bad_primes):
    dp = [[0] * (len(bad_primes) + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        min_prime = min_prime_divisor(i)
        if min_prime not in bad_primes:
            for j in range(len(bad_primes), -1, -1):
                dp[i][j] = max(dp[i-1][j], dp[i-1].index(min_prime) + 1 if j == 0 else dp[i-1][j-1])
        else:
            dp[i][j] = dp[i-1][j]
            
    return dp[-1][-1]

n, m = map(int, input().split())
bad_primes = list(map(int, input().split()))
print(max_beauty(n, bad_primes))
