import heapq

def beauty_of_array(n, m, bad_primes, numbers):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        max_beauty = float('-inf')
        for j in range(i):
            if numbers[j] not in bad_primes:
                gcd_val = reduce_gcd(numbers[j:i+1])
                beauty = dp[j] - numbers[j-1] * (i - j) + gcd_val
                max_beauty = max(max_beauty, beauty)
        dp[i] = max_beauty
    return dp[-1]

def reduce_gcd(nums):
    gcd_val = nums[0]
    for num in nums[1:]:
        while gcd_val % num:
            gcd_val //= gcd(gcd_val, num)
    return gcd_val

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

n, m = map(int, input().split())
bad_primes = list(map(int, input().split()))
numbers = list(map(int, input().split()))
print(beauty_of_array(n, m, bad_primes, numbers))
