def find_subset_sum(n, m, elements):
    # Initialize the dp array
    dp = [[False for _ in range(m)] for _ in range(n + 1)]

    # Base case: there is a subset with sum 0 (empty set)
    for i in range(m):
        dp[0][i] = True

    # Fill up the dp array
    for i in range(1, n + 1):
        for j in range(m):
            if elements[i - 1] <= j:
                dp[i][j] = (dp[i - 1][j] or (dp[i - 1][j - elements[i - 1]] and elements[i - 1] % m == 0))
            else:
                dp[i][j] = dp[i - 1][j]

    # Return whether there is a subset with sum equal to m
    return dp[n][m - 1]

# Read the input
n, m = map(int, input().split())
elements = list(map(int, input().split()))

# Print the output
print(find_subset_sum(n, m, elements))
