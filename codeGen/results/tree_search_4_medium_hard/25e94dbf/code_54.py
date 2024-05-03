def maximum_distance(commands, n):
    m = len(commands)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = 1

    for i in range(1, m + 1):
        j = 0
        while j <= min(i, n):
            if commands[i-1] == 'F':
                if j == 0:
                    dp[i][j] = dp[i-1][0] + 1
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
            elif commands[i-1] == 'T':
                if j == i:
                    dp[i][j] = dp[i-1][i-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j+1]) + 1
            j += 1

    return max(dp[m])
