def min_mana(n):
    k = [int(i) for i in input().split()]
    h = [int(i) for i in input().split()]

    dp = [[float('inf')] * (max(k) + 1) for _ in range(n)]
    memo = {}

    dp[0] = 0
    for i in range(1, n):
        for j in range(max(k[i-1], k[i]), -1, -1):
            if j < k[i]:
                dp[i][j] = min(dp[i-1][max(0, j-1)], h[i])
            else:
                dp[i][j] = min(dp[i-1][max(0, j-1)], h[i]) + (j > 0)

    return dp[n-1][-1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(min_mana(n))
