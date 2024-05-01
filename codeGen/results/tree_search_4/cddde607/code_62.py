def count_paths(arr, K):
    N = len(arr)
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    # Base case: dp[0][0][k] = (arr[0][0] <= k) ? 1 : 0
    dp[0][0][0] = arr[0][0] <= K

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            if arr[i][j] > K:
                dp[i][j][:] = [0]
            else:
                dp[i][j] = [(arr[i][j] <= k) * (dp[i-1][j][k-arr[i][j]] + dp[i][j-1][k-arr[i][j]]) for k in range(K+1)]

    return dp[-1][-1][-1]

K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(count_paths(arr, K))
