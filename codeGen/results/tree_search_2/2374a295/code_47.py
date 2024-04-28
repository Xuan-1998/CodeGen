def good_sequences(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base case: k = 1
    for i in range(2, n + 1):
        dp[i][1] = 1

    # Bottom-up approach
    for j in range(2, k + 1):
        for i in range(j - 1, n):
            for x in range(i // j + 1, i + 1):  # Iterate over divisors of x
                if i % x == 0:  # Check if current element is a divisor of x
                    dp[i][j] += dp[x][j - 1]

    return dp[n][k] % (10 ** 9 + 7)

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(good_sequences(n, k))
