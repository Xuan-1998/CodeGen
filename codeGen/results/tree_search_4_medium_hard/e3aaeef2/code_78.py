def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [-1] * (n + 1)
        dp[0] = -1
        for i in range(1, n + 1):
            for c in str(i):
                if c == '9':
                    dp[i] = 1
                    break
                dp[i] = max(dp[int(c)] + 1, len(str(i)))
        print((dp[n]) % (10**9 + 7))

solve()
