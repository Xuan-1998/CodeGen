def canPartition(arr, K, M):
    N = len(arr)
    dp = [[False] * (N // K + 1) for _ in range(N + 1)]

    for i in range(K, N + 1):
        if all(abs(arr[i-1] - arr[j]) <= M for j in range(i)):
            dp[i][K] = True

    for i in range(1, N + 1):
        for j in range(1, min(N // K + 1, i // (M+1)) + 1):
            if i < K*M:
                dp[i][j] = False
            elif all(abs(arr[i-1] - arr[j]) <= M and dp[j][K-1]):
                dp[i][j] = True

    return any(dp[N][j] for j in range(K, N // K + 1))

N, K, M = map(int, input().split())
arr = list(map(int, input().split()))
print(canPartition(arr, K, M))
