t, l, r = map(int, input().split())
mod = 10**9 + 7
dp = [float('inf')] * (r - l + 1)
dp[0] = 0

for i in range(l, r+1):
    for j in range(max(1, i-l), i):
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[j] + dp[(i-j)//2])
        else:
            dp[i] = min(dp[i], dp[j] + dp[(i+1)//2])

ans = 0
for i in range(l, r+1):
    ans += t*(dp[i] - l) % mod

print(ans % mod)
