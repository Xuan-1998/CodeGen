def solve():
    m, N = map(int, input().split())
    memo = {0: 1}

    def dp(n):
        if n not in memo:
            for i in range(m):
                n_i = max(0, n - arr[i])
                memo[n] = (memo.get(n, 0) + dp(n_i)) % (10**9 + 7)
            memo[n] %= (10**9 + 7)
        return memo[n]

    arr = list(map(int, input().split()))
    print(dp(N))

solve()
