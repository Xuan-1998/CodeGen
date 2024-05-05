def numSquares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = 1
        while j ** 2 <= i:
            dp[i] = min(dp[i], dp[i - j ** 2] + 1)
            j += 1

    return dp[n]

# Test your function
n = int(input())
print(numSquares(n))
