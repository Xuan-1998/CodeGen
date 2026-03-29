def solve():
    n, q = map(int, input().split())
    signs = list(input())

    cum_sum = [0]
    for sign in signs:
        if sign == '+':
            cum_sum.append(cum_sum[-1] + 1)
        else:
            cum_sum.append(cum_sum[-1] - 1)

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if signs[j - 1] == '+':
                dp[i][j] = cum_sum[j] - cum_sum[j - i]
            else:
                dp[i][j] = -cum_sum[j] + cum_sum[j - i]

    for _ in range(q):
        l, r = map(int, input().split())
        print(min(dp[l][r], dp[l][r - 1]))

if __name__ == '__main__':
    solve()
