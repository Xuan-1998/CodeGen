python
def get_prime_divisors(n):
    prime_divisors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            prime_divisors.append(i)
            n //= i
    if n > 1:
        prime_divisors.append(n)
    return prime_divisors

def get_smallest_prime_divisor(prime_divisors):
    return min(prime_divisors) if prime_divisors else None

def calculate_beauty(arr, bad_primes):
    total_beauty = 0
    for num in arr:
        prime_divisors = get_prime_divisors(num)
        smallest_prime_divisor = get_smallest_prime_divisor(prime_divisors)
        if smallest_prime_divisor not in bad_primes:
            total_beauty += len(prime_divisors) * (smallest_prime_divisor == 2 or smallest_prime_divisor % 3 != 0)
    return total_beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(calculate_beauty(arr, bad_primes))
