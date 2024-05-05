def count_binary_numbers_without_consecutive_ones(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        consecutiveOnesCount = bin(i).count('1')
        if consecutiveOnesCount == 0:
            dp[i] = dp[i - 1] + 1
        elif consecutiveOnesCount == 1:
            dp[i] = dp[i - 1]
        else:
            for j in range(consecutiveOnesCount):
                if bin(i)[2:j].count('1') % 2 != 0 and dp[i-j-1] >= 1:
                    dp[i] = dp[i-j-1] + 1
                    break
            else:
                dp[i] = dp[i - 1]

    return dp[n]
