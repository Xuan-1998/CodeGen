import sys

def num_squares(n):
    dp = [0x3f3f3f3f] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        j = int(i ** 0.5)
        while j >= 1:
            if i >= j ** 2:
                dp[i] = min(dp[i], dp[j ** 2] + 1)
            j -= 1
    return dp[n]

n = int(input())
print(num_squares(n))
