import sys

def solve(t, l, r):
    MOD = 10**9 + 7
    dp = [0] * (r + 1)
    
    for i in range(2, r + 1):
        min_comp = float('inf')
        for j in range(1, i):
            min_comp = min(min_comp, dp[j - 1] + i - j)
        dp[i - 1] = (dp[i - 1] + min_comp) % MOD
    
    result = 0
    for i in range(t):
        result = (result + dp[l - 1]) % MOD
    return result

t, l, r = map(int, input().split())
print(solve(t, l, r))
