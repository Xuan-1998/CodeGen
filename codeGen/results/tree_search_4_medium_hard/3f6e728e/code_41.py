T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))
    dp = [[0] * (C + 1) for _ in range(N + 2)]

    for i in range(1, N + 1):
        for j in range(C + 1):
            if j < U[i - 1]:
                dp[i][j] = sum(dp[k][i - 1] for k in range(U_k, j + 1))
            else:
                dp[i][j] = dp[i - 1][U_i - 1]

    for i in range(1, M + 1):
        for j in range(C + 1):
            if j >= L[i - 1]:
                dp[i][j] += sum(dp[k][i - 1] for k in range(L_k, j + 1))
            else:
                dp[i][j] = dp[i - 1][L_i - 1]

    print(*[dp[C]])
