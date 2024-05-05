def good_primes(arr):
    good_count = 0
    for num in arr:
        if is_good_prime(num):
            good_count += 1
    return good_count

def bad_primes(arr):
    bad_count = 0
    for num in arr:
        if is_bad_prime(num):
            bad_count += 1
    return bad_count

def min_prime_divisor(n):
    # Find the minimum prime divisor of n using a sieve or trial division
    pass

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes_list = list(map(int, input().split()))

    dp = {}
    for i in range(n):
        min_prime_divisor = min_prime_divisor(arr[i])
        if i > 0 and arr[i] // min_prime_divisor == arr[i-1] // min_prime_divisor:
            dp[i] = max(dp.get(i-1, 0), good_primes(arr[:i+1]) - bad_primes(arr[:i+1]))
        else:
            dp[i] = good_primes(arr[:i+1]) - bad_primes(arr[:i+1])
    return dp[n-1]

print(solve())
