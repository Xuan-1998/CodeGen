import sys
from math import log10

def min_operations(n, x):
    if x >= 10**(n-1):
        return -1
    
    dp = [0] * (n+1)
    
    for i in range(1, n+1):
        if i == 1:
            continue
        else:
            k = int(log10(i))
            dp[i] = min(dp[i-1], dp[k]+i//10**(k-1)-1)
    
    return dp[n]

n, x = map(int, input().split())
print(min_operations(n, x))
