def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    # Initialize the DP table
    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    # Fill in the DP table
    for l in range(2, n + 1):  # l is the length of the subarray
        for i in range(n - l + 1):
            j = i + l - 1
            # Check if the first and last elements can be combined
            if a[i] == a[j] and (l == 2 or dp[i + 1][j - 1] == l - 2):
                dp[i][j] = dp[i + 1][j - 1] + 1
            # Check all possible split points
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

    # Output the result
    print(dp[0][n - 1])

if __name__ == "__main__":
    main()
