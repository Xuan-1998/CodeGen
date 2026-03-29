def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[0] * (n + 1) for _ in range(q + 1)]

    ps = [0] * (q + 1)
    sign_sum = 0

    for i in range(n):
        if signs[i] == '+':
            sign_sum += 1
        else:
            sign_sum -= 1

    for i in range(1, q + 1):
        ps[i] = ps[i - 1] + (1 if signs[n - i] == '+' else -1)

    for i in range(1, q + 1):
        for j in range(i, -1, -1):
            dp[i][j] = min(dp[i - 1][j], ps[i] - ps[j])

    ans = [0] * (q + 1)
    for i in range(q, -1, -1):
        ans[i] = dp[i][0]
        if i > 0:
            dp[i][0] -= dp[i - 1][0]

    for i in range(q):
        print(ans[i])

solve()
