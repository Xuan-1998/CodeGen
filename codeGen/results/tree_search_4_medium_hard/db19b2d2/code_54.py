import sys

def solve():
    n, m, h = map(int, input().split())
    si = list(map(int, input().split()))
    
    dp = [[0.0] * 2 for _ in range(n+1)]
    dp[0][0] = 1.0
    
    for k in range(1, n+1):
        for i in range(min(k, si[h-1])+1):
            if i > 0 or k-i < n:
                dp[k][1] += min(i, k-i) / (si[h-1]) * (1 - min(i, k-i) / (n-k)) ** (k-i)
    
    return max(-1, dp[n][1])

print(solve())
