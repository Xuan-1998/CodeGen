def solve(n, p):
    dp = [[0, 0] for _ in range(n+2)]

    dp[1][0] = 1

    for i in range(2, n+2):
        j = p[i-1]
        if (i - 1) % 2 == 0:
            dp[i][0] = min(dp[j-1][0], dp[j-1][1])
            dp[i][1] = dp[i-1][0]
        else:
            dp[i][0] = dp[i-1][0]
            dp[i][1] = min(dp[j-1][0], dp[j-1][1])

    return min(dp[n+1][0], dp[n+1][1]) % 1000000007

n = int(input())
p = [int(x) for x in input().split()]
print(solve(n, p))
