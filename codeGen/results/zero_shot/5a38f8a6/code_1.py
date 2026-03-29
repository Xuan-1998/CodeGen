import math

def generate_perfect_squares(n):
    perfect_squares = []
    i = 1
    while True:
        square = i ** 2
        if square > n:
            break
        perfect_squares.append(square)
        i += 1
    return perfect_squares

def min_perfect_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = 1
        while j ** 2 <= i:
            dp[i] = min(dp[i], dp[i - j ** 2] + 1)
            j += 1

    return dp[n]

n = int(input())  # get input from stdin
print(min_perfect_squares(n))  # print the minimum number of perfect squares to stdout
