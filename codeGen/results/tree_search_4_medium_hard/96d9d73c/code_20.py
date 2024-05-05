def can_partition(K, M, N):
    A = [int(x) for x in input().split()]
    dp = [[False] * (K + 1) for _ in range(N + 1)]

    for i in range(1, K + 1):
        dp[i][i] = True

    for i in range(1, N + 1):
        for j in range(min(i, K), 0, -1):
            if not dp[j-1][j]:
                continue
            for k in range(j, i+1):
                if all(A[x] <= A[k] + M and A[y] >= A[k] - M for x in range(k)):
                    dp[i][j] = True
                    break

    return dp[N][K]

if __name__ == "__main__":
    N, K, M = map(int, input().split())
    print(can_partition(K, M, N))
