import sys
from collections import defaultdict

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n+1):
        if i <= 2:
            dp[i] = 1
        else:
            dp[i] = (dp[i-1] * i) % (10**8 + 7)
    
    ans = 1
    for _ in range(m):
        ans = (ans * (n - (_+1))) % (10**8 + 7)
    print(ans)
