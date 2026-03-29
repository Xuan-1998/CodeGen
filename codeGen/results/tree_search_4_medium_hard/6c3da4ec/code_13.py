def max_bitwise_or(n, s):
    memo = {0: 0}
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        if i % 2 == 0:
            j = i // 2
            while j >= 0 and s[j] == '1':
                j -= 1
            dp[i] = max(dp[i], dp[j] | int(s[j + 1:i].lstrip('0'), 2))
        else:
            j = (i - 1) // 2
            while j >= 0 and s[j] == '1':
                j -= 1
            dp[i] = max(dp[i], dp[j] | int(s[j + 1:i].lstrip('0'), 2))

    return bin(max(dp))[2:]
