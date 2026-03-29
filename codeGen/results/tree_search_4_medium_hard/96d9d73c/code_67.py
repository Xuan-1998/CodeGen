import sys

def can_partition(A, K, M):
    N = len(A)
    dp = [[False] * (K + 1) for _ in range(N + 1)]

    dp[0][0] = True

    for i in range(1, N + 1):
        for j in range(min(i, K), -1, -1):
            if A[i-1] <= M:
                dp[i][j] = dp[i-1][j]
            else:
                p = i
                while p > 0 and A[p-1] <= M:
                    p -= 1
                if p >= 0:
                    dp[i][j] = any(dp[k][j-1] for k in range(p+1, i))
                else:
                    dp[i][j] = dp[i-p][j-1]

    return dp[N][K]

if __name__ == "__main__":
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(can_partition(A, K, M))
