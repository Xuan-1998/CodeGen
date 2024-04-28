def goodSequences(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base case: the sequence of length 1 always has 1 good sequence.
    for i in range(1, n + 1):
        dp[i][1] = 1

    for j in range(2, k + 1):
        for i in range(j, n + 1):
            # If i is a multiple of both the previous number and j,
            if (i % (j // i)) == 0:
                dp[i][j] = dp[i][j - 1] + dp[i // (j // i)][j - 1]
            else:
                dp[i][j] = 0

    return sum(dp[n]) % 1000000007


# Read input from standard input
n, k = map(int, input().split())

print(goodSequences(n, k))
