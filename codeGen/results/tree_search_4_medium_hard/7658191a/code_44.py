def max_score(n, k, z, arr):
    dp = [[0] * (k + 1) for _ in range(n)]
    
    for i in range(1, n):
        for j in range(min(i - 1, k), 0, -1):
            # Calculate the maximum score at cell (i, j)
            move_right = dp[i - 1][j - 1] + arr[i]
            move_left = dp[i - 2][j - 1] + arr[i - 1] if i > 1 else 0
            dp[i][j] = max(move_right, move_left)
    
    return dp[-1][-1]

# Example usage:
n, k, z = map(int, input().split())
arr = list(map(int, input().split()))
print(max_score(n, k, z, arr))
