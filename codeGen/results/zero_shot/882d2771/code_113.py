def solve():
    t, l, r = map(int, input().split())
    dp = [0] * (r - l + 2)
    for i in range(1, r - l + 2):
        dp[i] = min(dp[i-1], i) + 1
    ans = 0
    for i in range(t):
        ans += t[i] * (dp[l+i] - l) % (10**9 + 7)
    print(ans)

if __name__ == "__main__":
    solve()
