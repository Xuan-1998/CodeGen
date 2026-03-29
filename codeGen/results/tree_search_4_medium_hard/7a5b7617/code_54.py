def steady_tables():
    T = int(input())  # Read test cases from stdin

    for _ in range(T):
        N, M = map(int, input().split())  # Read number of rows and columns
        dp = [[[0] * (M + 1) for _ in range(N + 1)] for _ in range(M + 1)]

        for i in range(N + 1):
            for j in range(M + 1):
                if i == 0:  # Base case: all cells are filled
                    dp[0][i][j] = 1
                elif j == 0:  # Edge case: leftmost column
                    dp[j][0][i] = 1
                else:
                    for k in range(j + 1):
                        if i > 0 and (dp[k][j - k][i - 1] or k > M):  # Filter out invalid states
                            continue
                        dp[j][i][k] = (dp[j][i][k] + dp[k][j - k][i - 1]) % (10**9 + 7)

        answer = sum(dp[i][-1][-1] for i in range(N + 1)) % (10**9 + 7)
        print(answer)  # Print the result to stdout

steady_tables()
