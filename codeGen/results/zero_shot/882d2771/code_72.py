import sys

def f(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + 1, 2) if (i & (i - 1)) == 0 else dp[i // 2] + 1
    return dp[n]

t = int(input())
l, r = map(int, input().split())
ans = 0
for i in range(t):
    ans += (i + 1) * f(l + i)
print(ans % (10**9 + 7))
