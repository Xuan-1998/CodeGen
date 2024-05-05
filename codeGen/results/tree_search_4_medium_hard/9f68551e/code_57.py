def min_mana(n, k, h):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        if k[i-1] == h[i-1]:
            dp[i][i-1] = h[i-1]
        else:
            dp[i][i-1] = max(dp[i-1][i-2], h[i-1])
    return dp[n][n-1]

t = int(input())
for _ in range(t):
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))
    print(min_mana(n, k, h))
