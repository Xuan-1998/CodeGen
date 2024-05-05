import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    MOD = 10**9 + 7
    
    dp = [0] * (n+1)
    dp[0] = 1
    
    for i in range(1, n):
        if a[i] % i == 0:
            dp[i] += dp[i-1]
        dp[i] %= MOD
    
    return dp[n-1]

print(solve())
