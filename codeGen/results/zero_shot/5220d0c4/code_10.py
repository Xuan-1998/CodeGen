def min_prime_divisor(num):
    if num < 2:
        return None
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return i
    return num

def array_beauty(arr):
    beauty = 0
    for num in arr:
        prime_divisor = min_prime_divisor(num)
        if prime_divisor is not None and prime_divisor in bad_primes:
            beauty -= prime_divisor
        else:
            beauty += prime_divisor
    return beauty

def max_array_beauty(n, m, arr, bad_primes):
    return max(array_beauty(arr[i:]))
    for i in range(n):

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))
print(max_array_beauty(n, m, arr, bad_primes))
