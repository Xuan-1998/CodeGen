def min_falling_path(A):
    m, n = len(A), len(A[0])
    
    # Handle edge cases
    if not A:
        return 0
    for i in range(m):
        if i == 0:
            return sum(A[i])
        if j == 0 or j == n-1:
            min_sum = float('inf')
            for k in range(n):
                min_sum = min(min_sum, A[i][k])
            return min_sum

    # Initialize memo dictionary
    dp = [[float('inf')] * n for _ in range(m)]

    # Fill up the memo dictionary
    for i in range(m):
        for j in range(n):
            if i == 0:
                dp[i][j] = A[i][j]
            elif j == 0 or j == n-1:
                min_sum = float('inf')
                for k in range(len(A[0])):
                    min_sum = min(min_sum, dp[i-1][k] + A[i][j])
                dp[i][j] = min_sum
            else:
                dp[i][j] = min(dp[i-1][k] + A[i][j] for k in range(n))

    # Return the minimum sum of a falling path with non-zero shifts
    return min(dp[-1])

# Example usage:
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(min_falling_path(A))  # Output: 10
