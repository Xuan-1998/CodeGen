import sys
from math import floor, ceil

def solve():
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        if n > 10**5:
            print(0)  # since the number of possible words is less than or equal to n^m
            continue
        
        dp = [0] * (n + 1)
        for i in range(n):
            for j in range(i+1, min(m, 2*i)+1):
                dp[j] += 1
        
        for i in range(min(m, 2*n), m+1):
            dp[i] += dp[i-1]
        
        print((dp[m]%1000000007))  # %10^8+7

solve()
