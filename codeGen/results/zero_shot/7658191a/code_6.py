def max_score(arr, k):
    n = len(arr)
    dp = [[0] * (k+1) for _ in range(n)]

    # Initialize base case
    for j in range(n):
        dp[0][j] = arr[j]

    for i in range(1, k+1):
        for j in range(i-1, n):
            dp[i][j] = max(dp[i-1][j+1] + arr[j+1], dp[i-1][j-1] + arr[j-1])

    # Find the maximum score
    max_score = 0
    for j in range(k, -1, -1):
        max_score = max(max_score, dp[k][j])

    return max_score

# Example usage:
n, k, z = map(int, input().split())
arr = list(map(int, input().split()))
print(max_score(arr, k))
