import sys

t, l, r = map(int, input().split())

def f(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(2, n + 1):
        dp[i][1] = i
        for j in range(2, i + 1):
            if i % 2 == 0:
                dp[i][j] = min(dp[i // 2][j - 1] + j, dp[i - i // 2][j])
            else:
                dp[i][j] = min(dp[(i + 1) // 2][j - 1] + j, dp[i - (i + 1) // 2][j])
    return sum(t * f(l + i) for i in range(r - l + 1)) % (10**9 + 7)

print(f(r))
