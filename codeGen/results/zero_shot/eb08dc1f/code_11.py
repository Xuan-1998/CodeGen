def solve():
    n = int(input())
    mod = 998244353
    dp = [0] * (n + 1)
    
    # Calculate number of blocks of length 1 to n
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 10
        else:
            dp[i] = dp[i - 1]
            for j in range(i):
                dp[i] += (dp[j] * 10**(i - j - 1))
    
    # Calculate the count of blocks of each length modulo mod
    print(*[(dp[i] % mod) for i in range(1, n + 1)], sep=' ')

solve()
