import sys
from collections import defaultdict

def dp(n):
    dp = [False] * (n + 1)
    dp[0] = True
    
    memo = defaultdict(bool)
    
    for i in range(1, n + 1):
        if i % 2 == 1:
            dp[i] = any(dp[j] for j in range(i // 2 + 1))
        else:
            dp[i] = all(memo[j] for j in range((i - 1) // 2 + 1))
        
        memo[i] = dp[i]
    
    return sum(1 for i in range(n + 1) if dp[i]) % 998244353

n = int(sys.stdin.read())
print(dp(n))
