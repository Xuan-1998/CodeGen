import sys

def beautyContest(t, l, r):
    mod = 10**9 + 7
    dp = [0] * (r + 1)
    
    for i in range(l, r + 1):
        if i == 1:
            continue
        min_cmps = float('inf')
        for j in range(1, i):
            k = i - j
            min_cmps = min(min_cmps, dp[j] + dp[k] + 1)
        dp[i] = min_cmps
    
    ans = 0
    for i in range(t):
        ans += dp[l + i]
    
    return str(int(ans % mod))

t, l, r = map(int, input().split())
print(beautyContest(t, l, r))
