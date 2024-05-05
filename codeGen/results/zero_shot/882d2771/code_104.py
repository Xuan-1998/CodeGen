import sys

def solve(t, l, r):
    dp = [0] * (r + 1)
    for i in range(2, r + 1):
        dp[i] = min(dp[i-1], i - 1)

    ans = sum((t * (dp[l+i-1] - (l+i-1))) % (10**9+7) for i in range(t))
    return ans

t, l, r = map(int, input().split())
print(solve(t, l, r))
