def count_good_sequences(n, k):
    # Initialize dp table with zeros
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Base case: when j = 1, there's only one good sequence
    for i in range(1, n + 1):
        dp[i][1] = 1

    # Fill up the dp table using the transition relationship
    for i in range(2, n + 1):
        for j in range(2, min(i, n) + 1):
            if i % j == 0:  # i is a multiple of j
                dp[i][j] = (dp[i - 1][j // i] or 0) + (dp[i][j - 1] or 0)
            else:
                dp[i][j] = 0

    # Compute the total count of good sequences modulo 10000
    return sum(dp[n][j] for j in range(1, k + 1)) % 1000000007
