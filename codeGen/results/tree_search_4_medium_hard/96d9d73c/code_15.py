import sys

def can_partition(K, M, A):
    N = len(A)
    dp = [[False] * (K+1) for _ in range(N+1)]

    dp[0][0] = True

    for i in range(1, N+1):
        for j in range(min(i, K), -1, -1):
            if dp[i-1][j-1]:
                if A[i-1] - A[i-K] <= M:
                    dp[i][j] = True
                else:
                    dp[i][j] = False

    return any(dp[N][i] for i in range(K, 0, -1))

K, M = map(int, input().split())
A = list(map(int, input().split()))
print(can_partition(K, M, A))
