import math

def is_perfect_square(x):
    sqrt_x = math.sqrt(x)
    return int(sqrt_x + 0.5) ** 2 == x

def min_perfect_squares(n):
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(1, n+1):
        if is_perfect_square(i):
            dp[i][1] = 1
        else:
            for j in range(2, i+1):
                if is_perfect_square(i-j):
                    dp[i][j] = min(dp[i-j][1] + 1, dp[i][j-1])

    k = 0
    while dp[n][k] == float('inf'):
        k += 1

    return k

n = int(input())
print(min_perfect_squares(n))
