def solve(t, l, r):
    MOD = 10**9 + 7
    dp = [0] * (r + 1)
    for i in range(2, r + 1):
        dp[i] = min(dp[i - 1] + 1, dp[i // 2] if i % 2 == 0 else dp[(i + 1) // 2])
    
    ans = t * dp[l]
    for i in range(l + 1, r + 1):
        ans += t
        if i <= l:
            ans -= i * (dp[i] - 1)
    
    return ans % MOD

t, l, r = map(int, input().split())
print(solve(t, l, r))
