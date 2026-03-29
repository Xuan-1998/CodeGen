def can_partition(arr, K, M):
    N = len(arr)
    dp = [[False] * (N + 1) for _ in range(N + 1)]

    # Initialize the DP table
    for i in range(1, N + 1):
        if arr[i-1] >= K:
            dp[i][1] = True

    for j in range(2, N + 1):
        for i in range(j - 1, -1, -1):
            for k in range(1, i):
                if abs(arr[k-1] - arr[0]) <= M and dp[k][j-1] and dp[i-k][j]:
                    dp[i][j] = True
                    break

    return dp[N][N]

# Example usage:
arr = [int(x) for x in input().split()]
K, M = map(int, input().split())
print(can_partition(arr, K, M))
