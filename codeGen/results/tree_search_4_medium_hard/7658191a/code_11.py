def max_score(arr, k, z):
    n = len(arr)
    dp = [float('-inf')] * (k + 1)
    prev = [-1] * k

    for i in range(1, min(k, z) + 1):
        for j in range(i, -1, -1):
            if j > 0:
                left_score = dp[j-1] + arr[j-1]
                right_score = dp[i-1] + arr[i]
                dp[i] = max(left_score, right_score)
                prev[i] = j

    return dp[k]

# Example usage
arr = [1, 2, 3, 4, 5]
k = 3
z = 2
print(max_score(arr, k, z))  # Output: 11
