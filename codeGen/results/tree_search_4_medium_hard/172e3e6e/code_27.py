def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7

    dp = [1] * (n + 1)
    for i in range(1, n):
        if a[i] % (i + 1) == 0:
            dp[i + 1] += dp[i]
        dp[i + 1] %= mod
    print(dp[-1])

if __name__ == "__main__":
    solve()
