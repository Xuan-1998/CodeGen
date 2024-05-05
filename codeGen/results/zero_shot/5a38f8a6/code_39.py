import math

def min_perfect_squares(n):
    dp = [float('inf')] * (n + 1)
    prev_squares = [-1] * (n + 1)

    for i in range(0, int(math.sqrt(n)) + 1):
        square = i ** 2
        while square <= n:
            if square == 0:
                dp[square] = 1
            else:
                if dp[square] > dp[square - i ** 2] + 1:
                    dp[square] = dp[square - i ** 2] + 1
                    prev_squares[square] = i ** 2

            square += 1

    return dp[n]

n = int(input())
print(min_perfect_squares(n))
