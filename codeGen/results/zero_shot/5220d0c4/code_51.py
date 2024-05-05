def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def beauty(num):
    min_divisor = 2
    while num % min_divisor != 0:
        min_divisor += 1
    is_bad_prime = any(1 for prime in bad_primes if prime == min_divisor)
    return -min_divisor if is_bad_prime else min_divisor

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

beauty_sum = 0
for num in arr:
    beauty_sum += beauty(num)

print(beauty_sum)
