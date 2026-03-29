import sys

def solve(t, l, r):
    MOD = 10**9 + 7
    dp = [0] * (r - l + 1)
    
    for n in range(l, r + 1):
        f_n = min(f_i for i in range(l, n+1))
        dp[n-l] = f_n
    
    ans = sum(t[i] * dp[i] for i in range(t))
    return int(ans % MOD)

t, l, r = map(int, input().split())
print(solve(t, l, r))
