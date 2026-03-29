def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def min_prime_divisor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            return i
    return n

def beauty(n, is_bad_prime):
    if not is_prime(n):
        return 0
    if is_bad_prime:
        return min_prime_divisor(n)
    else:
        return n - min_prime_divisor(n)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

max_beauty = 0
for num in arr:
    is_bad_prime = num in bad_primes
    max_beauty = max(max_beauty, beauty(num, is_bad_prime))

print(max_beauty)
