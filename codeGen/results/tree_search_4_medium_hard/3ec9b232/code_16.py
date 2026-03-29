import sys

def calculate_ways(n):
    MOD = 10**9 + 7
    dp = [0] * (1 << n)
    dp[0] = 1
    
    for i in range(1, n):
        for p in range((1 << n) - 1, -1, -1):
            next_p = (p | (1 << i))
            if not ((p & (1 << (i - 1))) and (p & (1 << i))):
                dp[next_p] += dp[p]
                dp[next_p] %= MOD
    
    return dp[-1]

n = int(input())
m = list(map(int, input().split()))
print(calculate_ways(n))
