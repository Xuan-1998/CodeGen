def min_sum(a):
    n, s = len(a), sum(a)
    dp = [float('inf')] * (s + 1)
    dp[0] = 0

    for i in range(n):
        for j in range(s, a[i]-1, -1):
            if dp[j-a[i]] != float('inf'):
                dp[j] = min(dp[j], dp[j-a[i]] + a[i]*j)

    return min(dp)
