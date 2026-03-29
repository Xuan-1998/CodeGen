def maxBitwiseOR(n, s):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            for k in range(j - i):
                or_val = int(s[k+1:j+1], 2) | int(s[0:k], 2)
                dp[i][j] = max(dp[i][j], or_val)

    return bin(max(max(row[n] for row in dp)))[2:]
