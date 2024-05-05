import math

def min_perfect_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = int(math.sqrt(i))
        while j >= 1:
            if i - j ** 2 >= 0:
                dp[i] = min(dp[i], dp[j ** 2] + 1)
            j -= 1

    return dp[n]

n = int(input())
print(min_perfect_squares(n))
