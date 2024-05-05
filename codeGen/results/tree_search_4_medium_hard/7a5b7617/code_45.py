def steadyTables(N, M):
    MOD = 1000000000
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Initialize base cases
    for i in range(N + 1):
        dp[i][0] = 1

    # Tabulate solutions for overlapping subproblems
    for j in range(1, M + 1):
        for i in range(N + 1):
            if i == 0:
                dp[i][j] = 1
            else:
                total_sum = sum(dp[k][j - 1] * (M - k) for k in range(i))
                dp[i][j] = (total_sum % MOD)

    # Use tabulated solutions to solve larger problems
    result = sum(dp[N][j] for j in range(M))
    return result

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(steadyTables(N, M) % MOD)
