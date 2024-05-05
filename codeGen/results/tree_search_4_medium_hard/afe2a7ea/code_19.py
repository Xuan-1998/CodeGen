def set_signal_powers(n):
    dp = {0: True}
    for i in range(1, n + 1):
        if i % 2 == 0:
            dp[i] = (dp[i // 2] and not dp[i - 1]) or dp[i - 1]
        else:
            dp[i] = (not dp[i - 1] and (i > 1)) or dp[i - 1]
    return dp[n] % 998244353

n = int(input())
print(set_signal_powers(n))
