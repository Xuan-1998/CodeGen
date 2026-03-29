from math import sqrt

def prime_sieve(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [p for p in range(2, n) if sieve[p]]

def max_beauty(nums, bad_primes):
    primes = prime_sieve(max(nums) + 10)
    good_primes = set([p for p in primes if p not in bad_primes])
    
    dp = [0] * (len(nums) + 1)
    for i in range(1, len(nums)+1):
        if nums[i-1] in good_primes:
            dp[i] = max(dp[i], dp[i-1] + min_primes[nums[i-1]])
        else:
            dp[i] = max(dp[i], dp[i-1] - 2)
    return max(dp)

def min_primes(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return i
    return num

n, m = map(int, input().split())
nums = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(nums, bad_primes))
