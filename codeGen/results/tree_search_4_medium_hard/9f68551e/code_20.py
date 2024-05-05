def min_mana(n, k, h):
    dp = [[float('inf')] * (max(k) + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for j in range(1, max(k) + 1):
            if j < k[i - 1]:
                dp[i][j] = min(dp[i - 1][max(0, j - 1)] + h[i - 1], dp[i][min(j, k[i - 1] - 1)])
            else:
                dp[i][j] = dp[i - 1][j - 1]
    
    return dp[n][k[-1]]

# Read input
n = int(input())
k = list(map(int, input().split()))
h = list(map(int, input().split()))

print(min_mana(n, k, h))
