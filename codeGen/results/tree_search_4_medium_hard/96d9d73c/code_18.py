code
import sys

def partition_array():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [[False for _ in range(K+1)] for _ in range(N+1)]

    for i in range(K):
        dp[i][j] = False

    for i in range(N):
        for j in range(min(i//K + 1, K), -1, -1):
            if (A[i] - A[0]) % (M+1) <= 0 and dp[i-1][j]:
                dp[i][j] = True

    return "Yes" if dp[N][K] else "No"

print(partition_array())
code
