import sys
from math import sqrt, ceil

def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            elif i > 0 and j > 0:
                k = ceil(sqrt(min(i, j)))
                for side_len in range(1, k + 1):
                    if i - side_len >= 0 and j - side_len >= 0:
                        dp[i][j] = min(dp[i][j], dp[max(0, i - side_len)][max(0, j - side_len)] + 1)
    
    return dp[n][m]

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    print(min_squares(n, m))
