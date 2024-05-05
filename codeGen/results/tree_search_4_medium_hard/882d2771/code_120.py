def solve():
    t, l, r = map(int, input().split())
    dp = [0] * (r - l + 1)
    for i in range(l - 1, r):
        dp[i - l + 1] = (i - l + 2) * (i - l + 1) // 2
        for j in range(l - 1, i):
            dp[i - l + 1] -= j * dp[j - l]
    return sum(t * dp[i] for i in range(l - 1, r))

print(solve())
