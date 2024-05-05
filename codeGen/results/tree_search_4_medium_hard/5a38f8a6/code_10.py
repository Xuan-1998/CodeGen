def min_perfect_squares(n):
    dp = [0] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if i * i <= n:
            dp[i * i] = 1
        for j in range(i * i, n + 1):
            if dp[j - i * i]:
                dp[j] = min(dp[j], dp[j - i * i] + 1)
    return dp[n]

# Test the function
n = int(input())
print(min_perfect_squares(n))
