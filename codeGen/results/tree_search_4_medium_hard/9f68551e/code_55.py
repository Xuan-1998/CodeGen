def solve(n, k, h):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i > 0:
            dp[i] = min(dp[i], k[i - 1]) + max(h[i - 1] - dp[i - 1], 0)
        else:
            dp[i] = h[0]
    return dp[-1]

n = int(input())
k = list(map(int, input().split()))
h = list(map(int, input().split()))
print(solve(n, k, h))
