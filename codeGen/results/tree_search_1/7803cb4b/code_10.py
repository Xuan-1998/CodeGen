def min_length_after_merges(n, a):
    dp = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1  # Base case: a single element has length 1

    # Fill the DP table
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            # Try merging the subarray [i...j] if the ends can be merged
            if a[i] == a[j]:
                for k in range(i, j):
                    if dp[i][k] == dp[k+1][j] and a[i] == a[k] + 1:
                        dp[i][j] = min(dp[i][j], dp[i][k] + 1)
                        break
            # Split the subarray and find the best result for each part
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])

    return dp[0][n-1]

# Read input from stdin
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Get the result and print to stdout
result = min_length_after_merges(n, a)
print(result)
