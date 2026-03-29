import sys

def alien_language(n, m):
    MOD = 10**8 + 7
    dp = [0] * (n // 2 + 1)
    dp[0] = 1
    
    for i in range(1, n // 2 + 1):
        if 2 * i <= n:
            dp[i] = sum(dp[:i])
        else:
            dp[i] = dp[n // 2 - 1]
    
    return pow(sum(dp), m, MOD)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(alien_language(n, m))
