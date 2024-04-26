def solve(n, a):
    dp = [[float('inf')] * n for _ in range(n)]  # Initialize DP table with infinity

    # Base case: single elements
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table
    for length in range(2, n + 1):  # length of the subarray
        for i in range(n - length + 1):
            j = i + length - 1
            # Case 1: If the subarray can be merged into one element
            if a[i] == a[j] and dp[i + 1][j - 1] == length - 2:
                dp[i][j] = 1
            # Case 2: Try splitting the subarray and solve independently
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

    # The answer is the minimum possible length of the entire array
    return dp[0][n-1]

# Read input
n = int(input())
a = list(map(int, input().split()))

# Solve the problem and print the answer
print(solve(n, a))
