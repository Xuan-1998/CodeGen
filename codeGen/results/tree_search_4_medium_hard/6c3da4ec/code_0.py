def max_bitwise_or(s):
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Base cases
    for i in range(n+1):
        if i == 0:
            dp[i][0] = 0
        elif i == 1:
            dp[0][i] = int(s[0], 2)
        else:
            dp[0][i] = dp[0][i-1] | int(s[i-1], 2)

    # Fill DP table from bottom-up
    for i in range(1, n+1):
        for j in range(i, n+1):
            if j - i >= 2:
                max_or = 0
                for k in range(i):
                    max_or = max(max_or, dp[k][i] | dp[i][j])
                dp[i][j] = max_or

    # Find maximum bitwise OR value without leading zeroes
    max_value = 0
    for i in range(n+1):
        if j - i >= 2:
            max_value = max(max_value, dp[i][n])

    return bin(max_value)[2:]
