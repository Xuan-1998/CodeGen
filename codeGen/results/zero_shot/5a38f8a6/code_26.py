def min_perfect_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    print("Creating dynamic programming array...")
    for i in range(1, n + 1):
        for j in range(1, int(i ** 0.5) + 1):
            if i - j * j >= 0 and dp[i - j * j] + 1 < dp[i]:
                dp[i] = dp[i - j * j] + 1

    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(min_perfect_squares(n))
