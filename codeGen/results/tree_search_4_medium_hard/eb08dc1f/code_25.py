def count_blocks(n):
    mod = 998244353
    dp = [[0] * (n + 1) for _ in range(10**6)]

    for i in range(10**6):
        for k in range(min(n, len(str(i))):
            for j in range(k, -1, -1):
                dp[i][k] = (dp[i][k] + int((str(i).zfill(n))[i-k+1:j+k].count('0') == 1)) % mod

    res = [0] * (n + 1)
    for k in range(n + 1):
        for i in range(10**(k-1) - 1, 10**k - 1):
            res[k] = (res[k] + dp[i][k]) % mod

    return ' '.join(str(i) for i in res)
