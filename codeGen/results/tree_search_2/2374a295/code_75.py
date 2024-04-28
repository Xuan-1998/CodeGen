def count_good_sequences():
    n, k = map(int, input().split())
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(i, n+1):
            if i % j == 0:
                if j > 1:
                    dp[i][j] = sum(dp[x][j] for x in range(j-1, -1, -1))
                else:
                    dp[i][j] = 1
                # Add all the possible good sequences ending with i and having j as its last multiple divisor
                if j < n:
                    dp[i][j] += sum(dp[x][j+1] for x in range(i-1, -1, -1))
            else:
                dp[i][j] = 0

    return pow(10,9) + 7 - sum(dp[x][n] for x in range(1, n+1)) % (pow(10,9) + 7)
