def find_max_beaauty():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    max_beaauty = 0
    for x in arr:
        min_prime_divisor = None
        for p in range(2, x + 1):
            if is_prime(p) and x % p == 0:
                min_prime_divisor = p
                break
        if min_prime_divisor in bad_primes:
            beauty = -1
        else:
            beauty = 1
        max_beauty = max(max_beaauty, beauty)

    print(max_beauty)
