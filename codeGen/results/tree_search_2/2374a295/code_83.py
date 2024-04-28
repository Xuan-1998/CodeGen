def good_sequences(n, k):
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        if i % 2 == 0:
            dp[i] = dp[i // 2]
        elif i % 3 == 0:
            dp[i] = dp[i // 3]
        elif i % 4 == 0:
            dp[i] = dp[i // 4]
        else:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    dp[i] = (dp[j] * (i // j)) % (10**9 + 7)
                    break
    return dp[n] % (10**9 + 7)
