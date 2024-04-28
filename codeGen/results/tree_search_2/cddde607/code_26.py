def find_paths(K, N, arr):
    dp = [[0]*N for _ in range(N)]
    for i in range(N):
        dp[0][i] = 1 if arr[0][i] == K else 0
    for i in range(1, N):
        for j in range(N):
            if arr[i][j] == K:
                dp[i][j] = 1
            elif arr[i][j] < K:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) if i > 0 and j > 0 else 0
    return dp[N-1][N-1]

K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(find_paths(K, N, arr))
