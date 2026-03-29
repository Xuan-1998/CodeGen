def maximum_or(s):
    n = len(s)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if s[i - 1] == '1':
            dp[i] = dp[i - 1] | 1
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) if i > 1 else 0

    max_or = dp[-1]
    for i in range(1, n):
        for j in range(i + 1, n):
            left_or = dp[i]
            right_or = dp[j] ^ ((j - i) * (1 << (i.bit_length() - 1)))
            max_or = max(max_or, left_or | right_or)

    return bin(max_or)[2:]

# Example usage
s = input()
print(maximum_or(s))
