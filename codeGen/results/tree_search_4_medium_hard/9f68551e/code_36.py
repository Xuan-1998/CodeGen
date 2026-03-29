def solve():
    n = int(input())  # number of monsters
    k = list(map(int, input().split()))  # appearance times
    h = list(map(int, input().split()))  # healths

    dp = [[float('inf')] * (max(k) + 1) for _ in range(n)]
    dp[0][0] = 0

    for i in range(1, n):
        for j in range(max(k[i-1], k[i]) + 1):
            if j < k[i]:
                dp[i][j] = dp[i-1][max(0, j-1)] + (j > 0)
            else:
                dp[i][j] = min(dp[i-1][max(0, j-1)], h[i]) + (j > 0)

    return min(dp[-1])

print(solve())
