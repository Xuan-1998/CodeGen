def min_mana_required(n):
    dp = [[0] * (10**9 + 1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, 10**9 + 1):
            if j < k[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][k[i]-1]+h[i], dp[i-1][j])
    return dp[n-1][10**9]

n = int(input())
k = list(map(int, input().split()))
h = list(map(int, input().split()))

print(min_mana_required(n))
