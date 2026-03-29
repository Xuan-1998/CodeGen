import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def good_prime(p):
    if p in bad_primes:
        return False
    return True

n, m = map(int, input().split())
a = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if a[i-1] % j == 0:
            gcd = a[i-1]
            while gcd % j != 0:
                gcd = math.gcd(gcd, j)
            for p in bad_primes:
                if good_prime(p) and p <= gcd:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + a[i-1])
                elif p > gcd:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] - a[i-1])

print(dp[n][n])
