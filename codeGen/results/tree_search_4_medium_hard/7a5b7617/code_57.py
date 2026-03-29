import sys

T = int(input())  # Read T test cases from standard input

for _ in range(T):
    N, M = map(int, input().split())  # Read N and M for each test case
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Initialize the first row as M+1
    for j in range(M + 1):
        dp[0][j] = 1

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1:  # First row is special (any sum is valid)
                dp[i][j] = min(j, M) + 1
            else:
                for k in range(i+1):  # Consider all possible sums from i+1 down to 0
                    if k + (i+1) <= j:  # Ensure the sum doesn't exceed M
                        dp[i][j] = (dp[i][j] + dp[k][j-1]) % 1000000000

    total_stable_tables = sum(dp[N][j] for j in range(M + 1)) % 1000000000
    print(total_stable_tables)
