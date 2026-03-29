import sys

def canPartition(N, K, M):
    A = list(map(int, input().split()))
    dp = [[False] * (K+1) for _ in range(N+1)]

    for i in range(N+1):
        dp[i][0] = True

    for i in range(1, N+1):
        for j in range(min(i, K), 0, -1):
            if A[i-1]-M <= A[0] <= A[i-1]+M and dp[i-1][j]:
                dp[i][j] = True
            else:
                dp[i][K-1] = True

    return dp[N][K]

N, K, M = map(int, input().split())
print(canPartition(N, K, M))
