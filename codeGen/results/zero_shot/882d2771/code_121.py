code
t, l, r = map(int, input().split())
mod = 10**9 + 7

dp = [0] * (r + 1)
for i in range(2, r + 1):
    dp[i] = min(dp[i-1] + 1, 1) if i % 2 == 0 else dp[i//2] + 1

ans = 0
for i in range(t):
    ans += i * (dp[l+i] - l)
print(ans % mod)
