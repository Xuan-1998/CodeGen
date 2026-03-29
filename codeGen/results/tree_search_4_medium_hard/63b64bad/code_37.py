def solve():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [-1] * (n + 1)
    dp[0] = 0

    for i in range(2, n + 1):
        x, y = 1, 0
        while x <= n and x > 0:
            x += a[x - 1]
            y += a[x - 1]
            x -= a[x - 1]
            y += a[x - 1]

        if x <= 0 or x > n:
            dp[i] = y
            break

    for i in range(2, n + 1):
        print(dp[i])
