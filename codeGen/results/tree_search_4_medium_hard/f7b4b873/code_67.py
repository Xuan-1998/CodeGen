def partition_palindromes(S):
    N = len(S)
    dp = [[[] for _ in range(N+1)] for _ in range(N+1)]

    for i in range(N+1):
        for j in range(i+1):
            if i == 0 and j == 0:
                dp[i][j] = [[]]
            elif i > 0 and j == 0:
                dp[i][j] = [dp[i-1][j]]
            elif i > 0 and j > 0:
                if S[j-1] == S[i-1]:
                    new_partitions = []
                    for prev_partition in dp[i-1][j-1]:
                        new_partitions.extend([prev_partition + [S[j-1:]]])
                    dp[i][j] = new_partitions
                else:
                    dp[i][j] = dp[i-1][j]

    return dp[N][N]
