import sys
from math import sqrt

def min_perfect_squares(n):
    dp = {0: 0}
    for i in range(1, n + 1):
        if i not in dp:
            j = int(sqrt(i))
            while j * j <= i:
                dp[i] = min(dp.get(i, j * j) + (i - j * j != 0), dp.get(i, j * j) + 1)
                j -= 1
    return dp[n]

n = int(sys.stdin.readline())
print(min_perfect_squares(n))
