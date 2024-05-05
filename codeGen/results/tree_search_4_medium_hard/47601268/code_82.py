def count_binary(n):
    dp = [[True] * (n+1) for _ in range(int(len(bin(n)))-1)]

    for i in range(2, n+1):
        for k in range(1, int(len(bin(i)))):
            if bin(i)[k-1:k] == '1' and bin(i)[k-1-k//2:k//2].count('1') >= 1:
                dp[k][i] = False
            else:
                dp[k][i] = dp[k-1][i//2]
    return sum(1 for i in range(n+1) if dp[-1][i])
