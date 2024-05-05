import sys
from math import sqrt

def leastNumberOfSquares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        j = int(sqrt(i))
        while j * j <= i:
            dp[i] = min(dp[i], dp[j * j - 1] + 1)
            j -= 1
    
    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(leastNumberOfSquares(n))
