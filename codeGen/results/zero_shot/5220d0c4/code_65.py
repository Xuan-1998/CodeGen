def max_beauty(arr, bad_primes):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    beauty = 0
    for num in arr:
        min_prime_divisor = num
        while not is_prime(min_prime_divisor):
            min_prime_divisor -= 1
        beauty = max(beauty, int(is_prime(min_prime_divisor) and min_prime_divisor not in bad_primes))
    return beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(arr, bad_primes))
