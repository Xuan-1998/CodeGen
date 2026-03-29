import sys

def solve():
    n = int(input())
    s = input()
    k = len(s) - n + 1
    
    dp = [0] * (n+1)
    
    for i in range(1, n+1):
        if s[i-k:i] == 'RGB'[s.index(s[i-k+1]) % 3]:
            dp[i] = dp[i-1]
        else:
            dp[i] = min(dp[i], dp[i-1] + 1)
    
    print(dp[-1])

for _ in range(int(input())): solve()
