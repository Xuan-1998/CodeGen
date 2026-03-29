def min_prime_divisor(n):
    if n < 2:
        return None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n

def is_bad_prime(n, bad_primes):
    return min_prime_divisor(n) in bad_primes

n, m = map(int, input().split())
arr = list(map(int, input().split()))
primes = list(map(int, input().split()))

bad_numbers = [x for x in arr if is_bad_prime(x, primes)]
good_numbers = [x for x in arr if x not in bad_numbers]

def calculate_beauty(good_numbers, bad_numbers):
    good_sum = sum(min_prime_divisor(x) for x in good_numbers)
    bad_sum = sum(min_prime_divisor(x) for x in bad_numbers)
    return good_sum - bad_sum

max_beauty = max(calculate_beauty(good_numbers, bad_numbers) for _ in range(len(arr)))
print(max_beauty)
