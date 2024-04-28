def count_good_sequences():
    n, k = map(int, input().split())
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Initialize the base case: a sequence of length 1 is always good
    for i in range(1, n + 1):
        dp[i][1] = 1

    for j in range(2, k + 1):
        for i in range(j - 1, n // (j - 1)):
            # For each possible ending number i, update the count of good sequences
            # that end at i with length j
            dp[i][j] = sum(dp[i - (p - 1), j - 1] for p in range(2, j))
            if i % (j - 1) == 0:
                dp[i][j] += 1

    # Calculate the total count of good sequences
    result = sum(dp[n // k][k:])
    return str(result % 1000000007)

print(count_good_sequences())
