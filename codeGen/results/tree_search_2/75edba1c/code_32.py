def count_subarrays(N, K, Arr):
    # Create a 2D table to store the DP states
    dp = [[0] * (K + 1) for _ in range(N)]

    # Initialize the first row of the table
    for k in range(K + 1):
        if Arr[0] <= k:
            dp[0][k] = 1
        else:
            dp[0][k] = 0

    # Fill up the rest of the table using DP
    for i in range(1, N):
        for k in range(K + 1):
            if Arr[i] <= k:
                dp[i][k] = dp[i-1][k] + (1 if dp[i-1][k-Arr[i]] else 0)
            else:
                dp[i][k] = dp[i-1][k]

    # The answer is the sum of all values in the last row of the table
    return sum(dp[-1])

# Read input from stdin
N, K = map(int, input().split())
Arr = list(map(int, input().split()))

# Print the output to stdout
print(count_subarrays(N, K, Arr))
