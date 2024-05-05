import sys
from collections import deque

def calculate_max_joys(a, b, c):
    n = len(a)
    dp = [0] * (n + 1)
    
    for i in range(1, n):
        if i % 3 == 0:
            dp[i] = max(dp[i-1], dp[i-2] + a[i-1])
        elif i % 3 == 1:
            dp[i] = max(dp[i-1], dp[i-2] + b[i-1])
        else:
            dp[i] = max(dp[i-1], dp[i-2] + c[i-1])
    
    return dp[-1]

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, print.split()))
c = list(map(int, input().split()))

print(calculate_max_joys(a, b, c))
