def solve():
    t, l, r = map(int, input().split())
    dp = [0] * (r + 1)
    for i in range(2, r + 1):
        dp[i] = min(dp[i // 2] + 1) if i % 2 == 0 else dp[i - 1] + 1
    result = sum(t * pow(2, i - l) * (dp[i] - dp[l]) for i in range(l, r + 1))
    print(result % (10**9 + 7))

if __name__ == "__main__":
    solve()
