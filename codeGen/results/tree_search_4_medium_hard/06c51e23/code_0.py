def solve(n, t):
    dp = [0] * (n + 1)
    dp[1] = int(input().split('.')[1][0])

    for i in range(2, n + 1):
        time_taken = 1
        if dp[i - 1] > 0:
            time_taken += 9  # adding 9 seconds to round the previous digit
        round_value = min(int(float('1.' + input().split('.')[1][:i]) * (10 ** (n - i))), t)
        dp[i] = max(dp[i - 1], dp[i - 1] + round_value)

    return dp[n]
