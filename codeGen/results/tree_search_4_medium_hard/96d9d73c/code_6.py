def canPartition(K, M, N, arr):
    dp = [[False for _ in range(K+1)] for _ in range(N+1)]

    dp[0][0] = True

    for i in range(1, N+1):
        for j in range(1, min(i, K)+1):
            if arr[i-1]-M <= arr[0]+M:
                if j == 1 or arr[i-1]-M <= arr[0]+M and dp[0][j-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
            else:
                for p in range(i):
                    if A[p]-M <= A[i-1] <= A[p]+M and dp[p][max(0, j-1)]:
                        dp[i][j] = True
                        break

    return dp[N][K]
