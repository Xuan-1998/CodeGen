import math

def num_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(int(math.sqrt(i)) + 1):
            k = int(math.sqrt(j))
            if (j - k ** 2) >= 0 and dp[(j - k ** 2)] > 0:
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[n]

n = int(input())
print(num_squares(n))
