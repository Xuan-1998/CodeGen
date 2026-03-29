from collections import defaultdict

def solve():
    T = int(input())
    dp = [[[0] * 2001 for _ in range(2001)] for _ in range(2001)]
    rs = [[0] * 2001 for _ in range(2001)]
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == N:
            return 1

        res = 0
        for k in range(M, -1, -1):
            if rs[i-1][j-k] >= rs[i-1][j]:
                res += dp[i-1][j-k][k]
            else:
                break

        memo[(i, j)] = res
        return res

    N, M = map(int, input().split())
    for i in range(N):
        for j in range(M):
            rs[i][j] = int(input())

    ans = 0
    for i in range(N):
        for j in range(M):
            ans += dfs(i, j)
    print(ans % (10**9 + 7))

solve()
