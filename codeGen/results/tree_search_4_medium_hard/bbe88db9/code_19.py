def solve():
    n = int(input())
    p = [int(x) for x in input().split()]

    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][0] = 0
    dp[0][1] = -1

    for i in range(1, n + 1):
        for j in [p[i - 1], i]:
            if i == 1:  # Vasya starts at room 1
                if j == 1:
                    dp[i][0] = min(dp[i][0], dp[j][0] + 1)
                    dp[i][1] = -1
                else:
                    dp[i][0] = min(dp[i][0], dp[j][1] + 1)
            elif dp[i - 1][1] == 1:  # cross_count % 2 == 1, use second portal
                if j == p[i]:
                    dp[i][0] = min(dp[i][0], dp[j][0] + 1)
                    dp[i][1] = -1
                else:
                    dp[i][0] = min(dp[i][0], dp[j][1] + 1)
            else:  # cross_count % 2 == 0, use first portal
                if j == p[i]:
                    dp[i][0] = min(dp[i][0], dp[j][0] + 1)
                    dp[i][1] = -1
                else:
                    dp[i][0] = min(dp[i][0], dp[j][1] + 1)

    return dp[n + 1][0]

print(solve())
