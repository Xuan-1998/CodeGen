def count_portal_moves(n, portals):
    dp = [0] * (n + 1)
    dp[0] = n + 1

    for i in range(1, n + 1):
        if i % 2 == 1:  # ceiling has an odd number of crosses
            dp[i] = min(dp[portals[i - 1]] + 1, dp[i - 1])
        else:
            dp[i] = min(dp[i - 1], dp[portals[i - 2]])

    return dp[n] % 1000000007

n = int(input())
portals = [int(x) for x in input().split()]
print(count_portal_moves(n, portals))
