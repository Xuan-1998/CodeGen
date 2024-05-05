import sys
input = sys.stdin.readline

t, l, r = map(int, input().split())

dp = [0] * (r - l + 1)

for i in range(l, r):
    dp[i - l] = min(dp[k] for k in range(i) if l <= k < i) + 1

ans = 0
for i in range(t):
    ans += dp[i]

print(ans % (10**9 + 7))
