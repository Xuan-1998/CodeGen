def solve():
    t, l, r = map(int, input().split())
    dp = [0] * (r - l + 1)
    for i in range(l - 1, r):
        j = max(k for k in range(i - l + 2) if i - k <= r)
        dp[i - l + 1] = dp[j - l] + 1
    ans = 0
    for i in range(t):
        ans += (dp[l + i] * t) % (10**9 + 7)
    print((ans - (l * dp[r])) % (10**9 + 7))

if __name__ == "__main__":
    solve()
