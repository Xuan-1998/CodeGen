def can_partition(A):
    N = len(A)
    K = int(input())
    M = int(input())

    dp = [[False] * (K + 1) for _ in range(N + 1)]

    for i in range(K + 1):
        dp[0][i] = True

    for i in range(1, N + 1):
        for j in range(1, min(i, K + 1)):
            if dp[i - 1][j]:
                if abs(A[i - 1] - A[i]) <= M:
                    dp[i][j] = True
                else:
                    for k in range(j - 1, 0, -1):
                        if dp[i - 1][k]:
                            dp[i][j] = True
                            break

    return dp[N][K + 1]

if __name__ == "__main__":
    A = list(map(int, input().split()))
    print(can_partition(A))
