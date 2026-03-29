from collections import defaultdict

def f(r):
    dp = [[0] * (r + 1) for _ in range(2)]

    for k in range(1, r + 1):
        if k % 2 == 0:
            dp[1][k] = min(dp[0][k // 2], dp[0][k - 1]) + 1
        else:
            dp[1][k] = min(dp[0][k], dp[0][k - 1]) + 1

    return sum(min(dp[i][r - i] for i in range(2)) for _ in range(t))

t, l, r = map(int, input().split())
print(f(r) % (10**9 + 7))
