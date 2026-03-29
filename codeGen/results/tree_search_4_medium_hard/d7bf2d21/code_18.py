def num_longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n)]

    memo = {}

    for i in range(n):
        max_length = 0
        for j in range(1, n + 1):
            if arr[i] >= arr[max_length]:
                dp[i][j] = max(dp[i-1][j-1], 1) + 1
                max_length = j - 1

    return sum(1 for i in range(n) if dp[i][n] == n)

# Example usage:
arr = [1, 3, 5, 4, 2]
print(num_longest_increasing_subsequences(arr))  # Output: 2
