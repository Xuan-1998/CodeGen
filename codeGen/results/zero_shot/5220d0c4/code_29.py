def min_prime_divisor(n):
    if n <= 1:
        return None
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n

def is_good_prime(p, primes):
    return p not in primes

def beauty(arr, primes):
    total_beauty = 0
    for num in arr:
        min_divisor = min_prime_divisor(num)
        if is_good_prime(min_divisor, primes):
            total_beauty += 1
        else:
            total_beauty -= 1
    return total_beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
primes = list(map(int, input().split()))

max_beauty = 0
for i in range(2 ** len(arr)):
    subset_arr = [num for j, num in enumerate(arr) if (i & (1 << j)) == 0]
    max_beauty = max(max_beauty, beauty(subset_arr, primes))

print(max_beauty)
