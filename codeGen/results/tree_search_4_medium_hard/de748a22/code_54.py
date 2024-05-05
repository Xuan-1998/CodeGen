def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for l in range(1, n + 1):
        for r in range(l, n + 1):
            ans = n - l + r
            pos, neg = 0, 0

            for i in range(l - 1, r):
                if signs[i] == '+':
                    pos += 1
                else:
                    neg += 1

                ans -= (pos - neg)

            dp[l][r] = min(ans, dp[l - 1][r - 1])

    for _ in range(q):
        l, r = map(int, input().split())
        print(dp[l][r])

if __name__ == "__main__":
    solve()
