def max_xor_sum(A, X):
    N = len(A)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(i, -1, -1):
            if i == 1:
                dp[i][j] = A[0]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + (A[i-1] ^ A[j-1]))

    return dp[N][0]

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max_xor_sum(A, X))
