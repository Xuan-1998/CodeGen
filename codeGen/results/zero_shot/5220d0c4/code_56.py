def beauty(n):
    if n <= 1:
        return 0
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            if is_good_prime(p):
                return p
            else:
                return -1
    return 1

def is_good_prime(p):
    # to be implemented later
    pass

n, m = map(int, input().split())
array = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

beauties = [beauty(x) for x in array]
max_beauty = max(beauties)

print(max_beauty)
