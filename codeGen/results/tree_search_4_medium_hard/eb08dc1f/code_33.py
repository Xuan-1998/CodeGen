def count_blocks(n):
    MOD = 998244353
    dp = [[0] * (n + 1) for _ in range(11)]

    # Base case: single-digit numbers have no blocks
    for i in range(10):
        dp[i][1] = 1

    for len_ in range(2, n + 1):
        for digit in range(10**(len_-1), 10**len_):
            for j in range(1, min(len_, 10)):
                for k in range(max(0, len_-j), len_+1):
                    dp[digit][j] += dp[max(0, digit // (10**(k-1)) % 10)][min(j, 10**(len_-1)-1)]
                    dp[digit][j] %= MOD
        for j in range(len_ + 1):
            print(dp[j], end=' ')
    print()

count_blocks(int(input()))
