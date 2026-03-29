def solve():
    T = int(input())  # Read number of test cases

    for _ in range(T):
        N, M = map(int, input().split())  # Read N and M
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        dp[0][j] = 1 for j in range(M + 1)]

        for i in range(1, N + 1):
            for j in range(min(i, M) + 1):
                dp[i][j] = (dp[i - 1][j] + (M * dp[i - 1][max(0, j - M)]) % 1000000000

        print(sum(dp[-1]) % 1000000000)  # Print the sum of all values in the last row
