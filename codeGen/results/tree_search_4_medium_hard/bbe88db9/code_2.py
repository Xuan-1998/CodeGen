def solve(n):
    dp = [[float('inf')] * 2 for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        p = int(input()) - 1
        first_portal_moves = dp[p][0] + (int(input()) % 2)
        second_portal_moves = dp[p][1] + 1
        dp[i][0] = min(dp[i-1][0], first_portal_moves)
        dp[i][1] = min(dp[i-1][1], second_portal_moves)

    return min(dp[-1])
