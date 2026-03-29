from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n, k, z = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))

    dp = [[0] * (k + 1) for _ in range(n)]
    for i in range(1, n):
        dp[i][0] = arr[i - 1]

    for j in range(1, k + 1):
        for i in range(j, n):
            dp[i][j] = max(dp[max(0, i - z)][j - 1], dp[i - 1][j - 1] + arr[i])

    max_score = dp[-1][-1]
    print(max_score)
