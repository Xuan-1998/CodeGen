def min_prime_divisor(n):
    # Use trial division or Sieve of Eratosthenes to find the minimum prime divisor
    pass

def is_good_prime(p, bad_primes):
    return p not in bad_primes

def calculate_beauty(arr, bad_primes):
    beauty = 0
    for num in arr:
        min_prime_divisor = min_prime_divisor(num)
        if is_good_prime(min_prime_divisor, bad_primes):
            beauty += 1
        else:
            beauty -= 1
    return beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

max_beauty = calculate_beauty(arr, bad_primes)
print(max_beauty)
