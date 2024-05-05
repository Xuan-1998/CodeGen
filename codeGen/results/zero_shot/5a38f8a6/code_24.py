python
def min_perfect_squares(n):
    dp = {i: float('inf') for i in range(n+1)}
    dp[0] = 0

    for i in range(1, n+1):
        j = 1
        while j*j <= i:
            if i - j*j >= 0:
                dp[i] = min(dp[i], dp[i-j*j]+1)
            j += 1

    return dp[n]
