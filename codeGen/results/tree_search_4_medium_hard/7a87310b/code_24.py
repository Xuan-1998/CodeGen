def solve(N):
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, min(i, N) + 1):
            if i == j:
                # For a 2x2 matrix with trace i and positive determinant,
                # the number of matrices is simply 1.
                dp[i][j] = 1
            else:
                # The number of matrices with trace i and positive determinant
                # is the sum of the number of matrices with traces j-1, j+1
                # (if they exist) minus the number of matrices with trace j-1
                if j - 2 >= 0:
                    dp[i][j] = dp[j-2][j-1]
                else:
                    dp[i][j] = 1

    return sum(dp[N])

T = int(input())
for _ in range(T):
    N = int(input())
    print(solve(N))
