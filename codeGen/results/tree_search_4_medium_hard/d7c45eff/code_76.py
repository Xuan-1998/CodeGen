from collections import defaultdict
import sys

def solve():
    n, k = map(int, input().split())
    s = input()
    
    dp = defaultdict(str)
    dp[0] = ''
    
    for i in range(n):
        if len(dp[i]) < k:
            dp[i+1] = dp[i] + (s[i] if i < n-1 else '')
        else:
            break
    
    if len(s) == 1 or k <= n:
        print(min(s[:k], s + s[:k-n+1]))
    else:
        for j in range(k, 0, -1):
            if dp[j] == '':
                print(min(dp[j-1], s[:j-1] + (s[-2] if j > 1 else '')))
                break
