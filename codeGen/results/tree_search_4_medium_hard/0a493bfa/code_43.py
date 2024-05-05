def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            j = 2
            while i * j <= n and n % (i * j):
                j += 1
            factors.extend([i] * j)
        else:
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def beauty(a, b):
    n = len(a)
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        last_good_prime = -1
        for j in range(i-1, -1, -1):
            if a[j] not in b:
                last_good_prime = a[j]
                break
        if last_good_prime == -1:
            dp[i] = dp[i-1]
        else:
            pivot_gcds = [0] * (i + 1)
            for k in range(i, -1, -1):
                if a[k] != last_good_prime:
                    pivot_gcds[k] = gcd(pivot_gcds[k-1] if k > 0 else last_good_prime, a[k])
                else:
                    pivot_gcds[k] = dp[k-1]
            dp[i] = sum(pivot_gcds) + last_good_prime

    return dp[-1]

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(beauty(a, b))
