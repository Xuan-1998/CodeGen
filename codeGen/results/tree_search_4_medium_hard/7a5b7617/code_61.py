# Read input
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    # Initialize dp table with zeros
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Base case: one row can be filled in only one way
    for j in range(M + 1):
        dp[1][j] = 1

    # Fill up the dp table using dynamic programming
    for i in range(2, N + 1):
        for j in range(1, M + 1):
            # If the sum of elements in the ith row is greater than or equal to
            # the sum of elements in the (i-1)th row, we can add all possible ways
            # to fill the ith row without exceeding its sum.
            if j >= i:
                dp[i][j] = sum(dp[i-1][k] for k in range(i)) % 1000000000
            else:
                dp[i][j] = 0

    # The number of different steady tables is stored in the last cell of the table
    print(dp[N][M])
