import sys

def dp(s, t, memo):
    if (s, t) in memo:
        return memo[(s, t)]
    
    n = len(t)
    m = len(s)
    
    if n < m or not s in t[n-m:]:
        return -1
    
    res = 0
    for i in range(n-m+1):
        if t[i:i+m] == s:
            res += 1
            memo[(s, t[:i])] = dp("", t[:i], memo)
            break
    else:
        res += 1 + dp(s, t[m:], memo)
    
    return res

n = int(input())
for _ in range(n):
    t = input().strip()
    s = [input().strip() for _ in range(n)]
    
    memo = {}
    print(dp("", t, memo))
