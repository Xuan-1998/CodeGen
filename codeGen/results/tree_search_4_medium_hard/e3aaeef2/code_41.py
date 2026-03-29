def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = {}
        def dfs(n):
            if (n,) in dp:
                return dp[(n,)]
            if n < 10:
                res = m + 1
            else:
                last_digit = n % 10
                if last_digit < 9:
                    res = dfs(n // 10) + 1
                else:
                    res = dfs((last_digit - 1) * 10) + 1
            dp[(n,)] = res
            return res
        print(dfs(n) % (10**9 + 7))

if __name__ == "__main__":
    solve()
