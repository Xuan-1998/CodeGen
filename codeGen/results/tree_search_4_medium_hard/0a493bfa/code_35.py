import math

def max_beauty(remaining_nums):
    # Base case: If there are no more numbers left, return 0
    if not remaining_nums:
        return 0
    
    # Initialize maximum beauty and operations to 0
    max_b = 0
    op_count = 0
    
    for i in range(len(remaining_nums)):
        for j in range(i+1, len(remaining_nums)):
            gcd = math.gcd(remaining_nums[i], remaining_nums[j])
            
            if gcd not in bad_primes:
                beauty = max_beauty([x // gcd for x in remaining_nums if x % gcd == 0]) + sum(x % gcd != 0 for x in remaining_nums)
                if beauty > max_b:
                    max_b = beauty
                    op_count = len(remaining_nums) - i
    
    return (max_b, op_count)

def solve(n, m, a, bad_primes):
    dp = {}
    
    for i in range(n):
        beauty, _ = max_beauty(a[:i] + a[i+1:])
        if bad_primes:
            beauty -= sum(x % bad_primes[0] != 0 for x in a[:i])
        
        dp[i] = (beauty, len(bad_primes))
    
    return max(beauty for beauty, _ in dp.values())

n, m = map(int, input().split())
a = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(solve(n, m, a, bad_primes))
