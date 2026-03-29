def sequence_simulation(n, seq):
    dp = [[-1]*n for _ in range(n)]
    dp[0][0] = 0

    for i in range(2, n+1):
        if seq[i-1] > 0:
            dp[i-1][i-1] = max(dp[i-1][i-1], dp[i-2][i-2-seq[i-1]] + seq[i-1])
        else:
            dp[i-1][i-1] = -1

    for i in range(1, n):
        if seq[i] > 0 and dp[i-1][i-1] != -1:
            dp[i][i+seq[i]-1] = max(dp[i][i+seq[i]-1], dp[i-1][i-seq[i]] + seq[i])
        else:
            dp[i][i] = -1

    res = []
    for i in range(2, n+1):
        if dp[i-1][i-1] != -1:
            res.append(dp[i-1][i-1])
        else:
            res.append(-1)

    return res


n = int(input())
seq = list(map(int, input().split()))
print(*sequence_simulation(n, seq), sep='\n')
