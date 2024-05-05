def count_numbers_without_consecutive_ones(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        binary_str = bin(i)[2:]
        has_consecutive_ones = any(binary_str[j] == '1' and binary_str[j+1] == '1' for j in range(len(binary_str) - 1))
        if not has_consecutive_ones:
            dp[i] = sum(dp[:i]) + 1
        else:
            dp[i] = 0

    return dp[n]
