def min_cuts(s):
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            if s[j:i].endswith(s[i:j:-1]):
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[n]

print(min_cuts(input()))
