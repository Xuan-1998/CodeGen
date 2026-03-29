from math import ceil
import sys

MOD = 10**9 + 7

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = [0] * (n+2)
    dp[1] = 1
    
    for i in range(2, n+2):
        if i % 2 == 0:
            dp[i] = min(dp[p[i-1]], dp[ceil(i/2)] + 1)
        else:
            dp[i] = min(dp[p[i-1]], 1 + dp[ceil(i/2)])
    
    return dp[n+1]

print(solve())
