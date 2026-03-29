def beauty(s, bad_primes):
    if s == 1:
        return 0
    p = min([p for p in range(2, int(s**0.5) + 1) if s % p == 0 and p not in bad_primes])
    if p not in bad_primes:
        return beauty(s // p, bad_primes) + s
    else:
        return beauty(s // p, bad_primes) - s

def maximize_beauty():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    # Initialize the maximum beauty
    max_beauty = 0

    # Iterate through the array and perform operations
    for i in range(n):
        for j in range(i + 1, n):
            gcd = a[i]
            for k in range(j + 1, n):
                gcd = abs(gcd * a[k] // math.gcd(a[i], a[k]))
            max_beauty = max(max_beauty, beauty(gcd, bad_primes))

    print(max_beauty)
