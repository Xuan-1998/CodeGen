import sys
from collections import defaultdict

def solve(m, N, A):
    MOD = 10**9 + 7
    
    # Initialize dp dictionary with default values (0)
    dp = defaultdict(int)
    
    for num in A:
        for i in range(N, num - 1, -1):
            dp[i] += dp.get(i - num, 0) % MOD
        dp[0] = 1
    
    return dp[N] % MOD

# Read input from stdin
m, N = map(int, input().split())
A = list(map(int, input().split()))

print(solve(m, N, A))
