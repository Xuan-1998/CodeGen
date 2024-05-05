def count_ones(n):
    dp = [[0] * (len(str(n)) + 1) for _ in range(10)]

    for i in range(1, 10):
        dp[i][1] = 1

    for j in range(2, len(str(n)) + 1):
        for i in range(10):
            if j == 2:
                dp[i][j] = (i == 1) * 9
            else:
                dp[i][j] = (dp[i][j-1]) * 9 + (i == 1)

    return sum(sum(row) for row in dp)
