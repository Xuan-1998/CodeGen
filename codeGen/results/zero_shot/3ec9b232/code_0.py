def solve(n, m):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            if m[j] == i:
                dp[i] += dp[j]
        dp[i] %= 10**9 + 7

    return dp[n]

n = int(input())
m = list(map(int, input().split()))
print(solve(n, m))
