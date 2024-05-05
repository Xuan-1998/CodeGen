def solve(n, m):
    MOD = 10**9 + 7
    dp = {0: 1}

    def dfs(i):
        if i not in dp:
            cnt = 0
            while i > 0:
                last_digit = i % 10
                i //= 10
                cnt += 1
                i = (i * 10) + (last_digit + 1) % 10
            dp[i] = cnt
        return dp[i]

    return dfs(n) % MOD

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
