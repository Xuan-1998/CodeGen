import math

def min_perfect_squares(n):
    dp = [float('inf')] * (n+1)
    dp[0] = 0

    for i in range(1, int(math.sqrt(n))+1):
        if i*i <= n:
            dp[i*i] = 1
        for j in range(i*i, n+1):
            dp[j] = min(dp[j], dp[j-i*i] + 1)

    return dp[n]

n = int(input())
print(min_perfect_squares(n))
