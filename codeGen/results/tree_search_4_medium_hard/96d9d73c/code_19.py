def canPartitionArray(A, K, M):
    N = len(A)
    dp = [[False] * (N // K + 1) for _ in range(N + 1)]

    for i in range(K, N + 1):
        for j in range(1, (i - 1) // K + 1):
            if all(abs(A[k-1] - A[m-1]) <= M for k in range(j*K+1, min((j+1)*K, i)+1)):
                dp[i][j] = True
            else:
                dp[i][j] = False

    return any(dp[N])

# Test the function
N, K, M = map(int, input().split())
A = list(map(int, input().split()))
print(canPartitionArray(A, K, M))
