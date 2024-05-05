def solve():
    t, l, r = map(int, input().split())
    dp = [0] * (r + 1)
    for i in range(2, r + 1):
        if i % 2 == 0:
            dp[i] = dp[i // 2] + 1
        else:
            dp[i] = dp[(i - 1) // 2] + i // 2 + 1
    res = (t0 * dp[l]) + (t1 * dp[l + 1]) + ... + (tr * dp[r])
    print(res % (10**9 + 7))

if __name__ == "__main__":
    solve()
