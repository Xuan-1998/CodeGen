def solve():
    n = int(input())
    M = sorted(map(int, input().split()))
    MOD = 10**9 + 7

    dp = {i: [1] for i in range(n+1)}
    def dfs(i, j):
        if (i, j) in dp:
            return dp[(i, j)]
        res = 0
        for k in range(1, i+1):
            if M[j] == M[k-1]:
                res += dfs(k-1, j-1) + dfs(i-k, j-1)
        res %= MOD
        dp[(i, j)] = res
        return res

    res = 0
    for i in range(1, n+1):
        res += dfs(i, n-1)
    print(res % MOD)

if __name__ == '__main__':
    solve()
