import sys

def perfect_squares(n):
    dp = {0: 0}
    for i in range(1, n+1):
        dp[i] = float('inf')
        for j in range(int(i**0.5) + 1):
            if (j ** 2) <= i:
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[n]

n = int(sys.stdin.readline())
print(perfect_squares(n))
