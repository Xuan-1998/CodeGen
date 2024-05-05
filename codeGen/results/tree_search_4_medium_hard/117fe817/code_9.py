import math

def count_ones(n):
    dp = [0] * (math.floor(math.log10(n)) + 1)
    
    for i from 0 to log(n):
        dp[i] = dp[i-1] + (n // 10**i) * int('1' * (10**i))
        
    return sum(dp)

n = int(input())
print(count_ones(n))
