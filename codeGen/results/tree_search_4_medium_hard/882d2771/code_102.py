def solve(t, l, r):
    MOD = 10**9 + 7
    dp = [0] * (r + 1)
    for i in range(2, r + 1):
        dp[i] = min(dp[j] + 1 for j in range(i))
    return sum(t * dp[l + k - 1] for k in range(r - l + 1)) % MOD

t, l, r = map(int, input().split())
print(solve(t, l, r))
