def solve():
    T = int(input())
    MOD = 1000000000
    dp = [[0] * (2001) for _ in range(2001)]

    def dfs(i, j):
        if i == 0 or j == 0:
            return 1 % MOD
        if dp[i][j]:
            return dp[i][j]
        res = 0
        for k in range(i + 1):
            res += (k * dfs(i - k, j - 1)) % MOD
        dp[i][j] = res % MOD
        return res % MOD

    for _ in range(T):
        N, M = map(int, input().split())
        print(dfs(N, M))

if __name__ == "__main__":
    solve()
