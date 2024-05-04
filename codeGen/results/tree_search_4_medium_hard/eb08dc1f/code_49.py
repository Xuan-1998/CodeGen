def solve(n):
    MOD = 998244353
    dp = [[0] * (n + 1) for _ in range(10)]

    def helper(i, j):
        if j == 1:
            return 1
        if dp[i][j]:
            return dp[i][j]
        res = 0
        for prev_digit in range(10):
            if str(prev_digit) * (j + 1) <= '1' * n:
                res += helper(int(str(prev_digit) * (j + 1)), j)
        return dp[i][j] = res % MOD

    ans = [0] * (n + 1)
    for i in range(10):
        for j in range(1, min(j + 1, n + 1)):
            ans[j] += helper(i, j)
    print(*ans[:n], sep=' ')
