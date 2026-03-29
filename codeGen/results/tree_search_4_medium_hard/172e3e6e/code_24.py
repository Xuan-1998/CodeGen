def count_good_subsequences(n, a):
    MOD = 10**9 + 7
    memo = {0: 1}

    for i in range(1, n+1):
        if i % (i+1) == 0:
            dp_i = sum(memo[j]*((i-j)//j) for j in range(i) if i%j == 0)
            memo[i] = dp_i
        else:
            memo[i] = 0

    return sum(memo.values()) % MOD
