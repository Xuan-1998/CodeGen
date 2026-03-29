def can_partition(A):
    N = len(A)
    K = int(input())
    M = int(input())

    A.sort()

    dp = [[False] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(1, N + 1):
        for j in range(M + 1):
            if j >= A[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - A[i - 1]])
            dp[i][j] = dp[i][j] or (j == M and i >= K)

    return dp[N][M]

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(can_partition(A))
