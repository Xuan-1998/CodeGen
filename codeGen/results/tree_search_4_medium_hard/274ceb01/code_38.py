def min_marks_below_water(n, marks):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            if marks[j] < i:
                dp[i] = min(dp[i], dp[j] + i - marks[j])

    return dp[n]
