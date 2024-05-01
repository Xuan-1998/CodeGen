import sys
from math import gcd

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = 0
            else:
                min_squares = float('inf')
                for k in range(min(i, j), 0, -1):
                    if gcd(k, max(i, j)) == 1:
                        min_squares = min(min_squares, dp[i - k][j - k] + (i * j) // (k * k))
                        break
                dp[i][j] = min_squares

    return dp[n][m]

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(solve(n, m))
