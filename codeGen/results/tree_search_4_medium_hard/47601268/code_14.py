def count_non_consecutive_ones(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if bin(i)[2:] != '1' * len(bin(i)[2:]):
            dp[i] = dp[i - 1]
        else:
            last_zero_index = None
            for j, bit in enumerate(reversed(bin(i)[2:])):
                if bit == '0':
                    last_zero_index = j
                    break

            if last_zero_index is not None:
                dp[i] = dp[n - 1 - i] + dp[last_zero_index - 1]
            else:
                dp[i] = 0

    return dp[n]
