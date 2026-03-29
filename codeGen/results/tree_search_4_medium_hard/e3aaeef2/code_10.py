def solve():
    t = int(input())
    memo = {}
    for _ in range(t):
        n, m = map(int, input().split())
        if (n, m) in memo:
            print(memo[(n, m)] % 10**9 + 7)
        else:
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, n + 1):
                val = int(str(i))
                for j in range(1, min(i, m) + 1):
                    new_val = 0
                    for k in range(len(str(val))):
                        digit = (val // 10**(len(str(val)) - k - 1)) % 10
                        new_val += (digit + 1) * (10 ** (k))
                    dp[j][i] = len(str(new_val))
            memo[(n, m)] = dp[m][n]
            print(dp[m][n] % 10**9 + 7)

solve()
