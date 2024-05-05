def solve(n, s, a):
    dp = [[0] * (2*s+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, 2*s+1):
            if i == 1:
                dp[i][j] = a[0]
            else:
                dp[i][j] = min(dp[i-1][max(0, j-a[i-1])] + a[i-1], dp[i-1][j])

    return dp[n][s]

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, s, a))
