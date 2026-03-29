import sys

def solve():
    t, l, r = map(int, input().split())
    
    dp = [0] * (r + 1)
    dp[l-1] = 1
    for i in range(l, r+1):
        for j in range(2**(i-l), min(2**(i-l), r-i)+1)):
            dp[i] = min(dp[i], dp[j] + dp[i-j-1])
    
    return (t*sum(dp[i] for i in range(l, r+1)) - l*dp[r]) % (10**9 + 7)

print(solve())
