def count_numbers_without_consecutive_ones(n):
    dp = [False] * (n + 1)
    dp[0] = True  # base case: 0 has no consecutive ones

    for i in range(1, n + 1):
        prev_has_consecutive_ones = False
        if i - 1 >= 0:
            prev_has_consecutive_ones = dp[i - 1]

        current_binary = bin(i)[2:]
        has_consecutive_ones = any('11' in current_binary[:j] for j in range(1, len(current_binary) + 1))

        if not prev_has_consecutive_ones and not has_consecutive_ones:
            dp[i] = True
        else:
            dp[i] = False

    return sum(dp)

n = int(input())
print(count_numbers_without_consecutive_ones(n))
