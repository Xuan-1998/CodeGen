import sys

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j:  # perfect square
                dp[i][j] = 1
            elif is_perfect_square(i):
                dp[i][j] = dp[i-1][j]
            elif is_perfect_square(j):
                dp[i][j] = dp[i][j-1]
            else:
                k = min(i, j)
                while k > 0 and not (is_perfect_square(k) and is_perfect_square(k)):
                    k -= 1
                if k > 0:
                    dp[i][j] = 1 + dp[i-k][j-k]

    return dp[n][m]


def is_perfect_square(n):
    # This function checks whether a number is a perfect square or not.
    # You can implement this however you like, but it should be efficient.
    if n < 2:
        return True
    sqrt = int(n ** 0.5)
    return sqrt * sqrt == n


n, m = map(int, input().split())
print(min_squares(n, m))
