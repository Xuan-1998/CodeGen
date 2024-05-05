def solve():
    n = int(input())
    p = list(map(int, input().split()))
    dp = [[float('inf')] * 2 for _ in range(n + 1)]
    state = [[0] * 2 for _ in range(n + 1)]

    dp[1][0] = 0
    for i in range(2, n + 1):
        if p[i - 1] % 2 == 0:
            j = p[i - 1]
            k = i
        else:
            j = i
            k = p[i - 1]
        dp[i][0] = min(dp[j][1] + 1, dp[k][1] + 1)
        state[i][0] = (state[i - 1][0] + 1) % 2

    return dp[n + 1][1]

print(solve() % 1000000007)
