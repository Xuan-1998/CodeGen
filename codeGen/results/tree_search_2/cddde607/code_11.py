def find_paths(arr, N, K):
    dp = [[0 for _ in range(N)] for _ in range(N)]

    # Base case: when i == N-1 and j == N-1
    if arr[N-1][N-1] == K:
        dp[N-1][N-1] = 1
    else:
        dp[N-1][N-1] = 0

    for i in range(N-2, -1, -1):
        for j in range(N-2, -1, -1):
            if arr[i][j] == K and i == N-1 and j == N-1:
                dp[i][j] = 1
            else:
                dp[i][j] = 0

    # Fill the DP table top-down
    for i in range(N-2, -1, -1):
        for j in range(N-2, -1, -1):
            if arr[i][j] == K:
                dp[i][j] += dp[i+1][j]
                dp[i][j] += dp[i][j+1]

    return dp[0][0]

# Receive input from stdin
K, N = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(N)]

print(find_paths(arr, N, K))
