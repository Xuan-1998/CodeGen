import sys

def solve():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [[False] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(1, N + 1):
        for j in range(min(i, K), -1, -1):
            if A[i-1] - A[0] > M or i < K:
                dp[i][j] = False
            else:
                dp[i][j] = (dp[i-1][j-1] if j > 0 else True) and ((A[i-1] - A[i-K+1]) <= M)
        for j in range(K + 1):
            print(dp[i][j], end=' ')
        print()

    return 'YES' if dp[N][K] else 'NO'

print(solve())
