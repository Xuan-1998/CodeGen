import math

def prime_divisors(n):
    """Find all prime divisors of n"""
    divs = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            divs.append(i)
            n //= i
    if n > 1:
        divs.append(n)
    return divs

def beauty(num, bad_primes):
    """Calculate the beauty of a number"""
    prime_div = min(prime_divisors(num))
    is_bad_prime = prime_div in bad_primes
    return 1 if not is_bad_prime else -1

def max_beauty(arr, bad_primes):
    """Find the maximum beauty of an array"""
    max_beauty = 0
    for num in arr:
        beauty_val = beauty(num, bad_primes)
        if beauty_val > max_beauty:
            max_beauty = beauty_val
    return max_beauty

# Read input from stdin
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Calculate and print the maximum beauty
max_b = max_beauty(arr, bad_primes)
print(max_b)
