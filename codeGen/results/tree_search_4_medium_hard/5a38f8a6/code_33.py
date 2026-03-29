def min_perfect_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(int(i ** 0.5) + 1):
            if i >= j ** 2:
                dp[i] = min(dp[i], 1 + dp[i - j ** 2])

    return dp[n]

if __name__ == '__main__':
    n = int(input())
    print(min_perfect_squares(n))
