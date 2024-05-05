def solve():
    n = int(input())
    p = [int(x) for x in input().split()]

    dp = [[float('inf')] * (1 << 30) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        j = 0
        if not p[i - 1]:
            j += 1
        for k in range(2 ** (i - 1)):
            if (k >> (i - 1)) & 1:
                j ^= 1
            dp[i][j] = min(dp[i][j], dp[i - 1][k] + 1)
    return dp[n][0]

print(solve())
